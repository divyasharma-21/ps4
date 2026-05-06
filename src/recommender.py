from src.model import compute_score

PLATFORMS = ["Instagram", "YouTube"]

def get_best_option(content_row, activity_map, history_map, creator_map):
    creator = content_row.creator_id
    content_type = content_row.content_type

    best_score = -1
    best_platform = None
    best_time = None

    for platform in PLATFORMS:
        for (platform, time) in activity_map.keys():
            score = compute_score(
                creator, platform, content_type, time,
                activity_map, history_map, creator_map
            )

            if score > best_score:
                best_score = score
                best_platform = platform
                best_time = time

    return best_platform, best_time, best_score