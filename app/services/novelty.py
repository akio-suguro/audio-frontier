import numpy as np

def compute_novelty(similarities, metadata_list, query_tags=None):
    max_sim = np.max(similarities)
    avg_sim = np.mean(similarities)

    # ① 距離
    novelty_distance = 1 - max_sim

    # ② 密度
    novelty_density = 1 - avg_sim

    # ③ タグ新規性
    if query_tags:
        all_tags = set()
        for m in metadata_list:
            all_tags.update(m.get("tags", []))

        new_tags = [t for t in query_tags if t not in all_tags]
        tag_score = len(new_tags) / len(query_tags)
    else:
        tag_score = 0.0

    return (
        0.4 * novelty_distance +
        0.3 * novelty_density +
        0.3 * tag_score
    )