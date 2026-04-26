import os
from app.models.audio import extract_audio_features
from app.services.feature_engine import fuse_features
from app.vectorstore.faiss_index import FaissIndex

DATA_DIR = "app/data/raw"
DIM = 388

index = FaissIndex(dim=DIM)

vectors = []
metadata = []

count = 0

for root, _, files in os.walk(DATA_DIR):
    for file in files:
        if not file.endswith(".mp3"):
            continue

        path = os.path.join(root, file)

        try:
            audio_feat = extract_audio_features(path)

            text = "instrumental experimental music"
            vec = fuse_features(text, audio_feat)

            if vec is not None:
                vectors.append(vec)

                metadata.append({
                    "file": file,
                    "bpm": audio_feat["bpm"]
                })

                count += 1

                if count > 200:
                    break

        except Exception as e:
            print("error:", file, e)

    if count > 200:
        break


if len(vectors) == 0:
    raise ValueError("No vectors created!")

index.add(vectors, metadata)
index.save()

print("index built:", len(vectors))
