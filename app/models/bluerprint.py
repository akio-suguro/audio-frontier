def generate_blueprint(text: str, novelty: float):
    return {
        "title": f"Unheard Track ({round(novelty, 2)})",
        "concept": text,
        "tempo": "80-100 BPM",
        "mood": "experimental / unknown",
        "structure": "non-linear, evolving",
        "note": "This music does not exist in current datasets."
    }