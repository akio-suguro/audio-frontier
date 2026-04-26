import essentia.standard as es

def extract_audio_features(path: str):
    features, _ = es.MusicExtractor()(path)

    return {
        "bpm": float(features["rhythm.bpm"]),
        "loudness": float(features["lowlevel.average_loudness"]),
        "spectral_centroid": float(features["lowlevel.spectral_centroid.mean"]),
        "danceability": float(features.get("rhythm.danceability", 0.0)),
    }