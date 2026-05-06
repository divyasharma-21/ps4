def compute_score(creator, platform, content_type, time,
                  activity_map, history_map, creator_map):

    base = creator_map.get(creator, 1.0)

    activity = activity_map.get((platform, time), 0.5)

    historical = history_map.get(
        (creator, platform, content_type, time), 0.5
    )

    score = base * activity * historical

    # soft platform bias
    if content_type == "SHORT" and platform == "Instagram":
        score *= 1.05
    elif content_type == "LONG" and platform == "YouTube":
        score *= 1.05

    return score