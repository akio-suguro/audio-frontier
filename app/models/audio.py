import essentia.standard as es
import subprocess
import tempfile
import os

def safe_get(features, key, default=0.0):
    try:
        return float(features[key])
    except Exception:
        return default


def convert_to_wav(input_path):
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    tmp_path = tmp.name
    tmp.close()

    subprocess.run([
        "ffmpeg", "-y",
        "-i", input_path,
        "-ac", "1",
        "-ar", "44100",
        tmp_path
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return tmp_path


def extract_audio_features(path: str):
    wav_path = convert_to_wav(path)

    try:
        features, _ = es.MusicExtractor()(wav_path)

        return {
            "bpm": safe_get(features, "rhythm.bpm"),
            "loudness": safe_get(features, "lowlevel.average_loudness"),
            "spectral_centroid": safe_get(features, "lowlevel.spectral_centroid.mean"),
            "danceability": safe_get(features, "rhythm.danceability"),
        }

    finally:
        if os.path.exists(wav_path):
            os.remove(wav_path)
