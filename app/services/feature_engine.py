import numpy as np
from app.models.embedding import embed

def normalize(vec):
    norm = np.linalg.norm(vec)
    return vec / norm if norm > 0 else vec

def fuse_features(text: str, audio_features: dict = None):
    """
    semantic + audio の融合ベクトルを生成
    """
    # semantic（384次元）
    semantic_vec = embed(text)

    if audio_features is None:
        return normalize(semantic_vec)

    # audio特徴をベクトル化（例：Essentia）
    audio_vec = np.array([
        audio_features.get("bpm", 0),
        audio_features.get("loudness", 0),
        audio_features.get("spectral_centroid", 0),
        audio_features.get("danceability", 0),
    ], dtype=np.float32)

    # スケーリング
    audio_vec = audio_vec / (np.linalg.norm(audio_vec) + 1e-8)

    # concat
    fused = np.concatenate([semantic_vec, audio_vec])

    return normalize(fused)