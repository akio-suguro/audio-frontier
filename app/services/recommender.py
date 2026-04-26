import numpy as np
from app.services.feature_engine import fuse_features
from app.services.novelty import compute_novelty
from app.vectorstore.faiss_index import FaissIndex
from app.models.blueprint import generate_blueprint

DIM = 388  # 384 + audio(4)
index = FaissIndex(dim=DIM)

def recommend(text: str):
    # ① ベクトル化
    vec = fuse_features(text)

    # ② 近傍取得
    sims, ids = index.search(vec, k=10)
    neighbors_meta = [index.metadata[i] for i in ids]

    # ③ 未踏領域生成（外挿）
    if len(ids) > 0:
        nearest_vec = index.index.reconstruct(ids[0])
        novel_vec = vec + 0.2 * (vec - nearest_vec)
    else:
        novel_vec = vec

    # ④ スコア
    novelty = compute_novelty(sims, neighbors_meta)

    # ⑤ Blueprint生成
    blueprint = generate_blueprint(text, novelty)

    print("SIM:", sims[:3])
    print("NOVELTY:", novelty)

    return {
        "input": text,
        "novelty_score": float(novelty),
        "blueprint": blueprint,
        "neighbors": neighbors_meta[:3]
    }