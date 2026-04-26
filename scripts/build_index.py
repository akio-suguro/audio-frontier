import os
from app.models.audio import extract_audio_features
from app.services.feature_engine import fuse_features
from app.vectorstore.faiss_index import FaissIndex

DATA_DIR = "app/data/raw"
DIM = 388

index = FaissIndex(dim=DIM)

vectors = []
metadata = []

for file in os.listdir(DATA_DIR):
    if not file.endswith(".mp3"):
        continue

    path = os.path.join(DATA_DIR, file)

    try:
        audio_feat = extract_audio_features(path)

        text = "instrumental experimental music"
        vec = fuse_features(text, audio_feat)

        vectors.append(vec)

        metadata.append({
            "file": file,
            "bpm": audio_feat["bpm"]
        })

    except Exception as e:
        print("error:", file, e)

index.add(vectors, metadata)
index.save()

print("index built:", len(vectors))
