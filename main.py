print("STARTING PROGRAM")
import pandas as pd
from src.loader import load_data, preprocess
from src.recommender import get_best_option
from src.scheduler import decide_schedule
from src.model import compute_score

content, activity, history, creators = load_data()
activity_map, history_map, creator_map = preprocess(activity, history, creators)

results = []

for _, row in content.iterrows():

    best_platform, best_time, best_score = get_best_option(
        row, activity_map, history_map, creator_map
    )

    current_time = row.created_timestamp

    current_score = compute_score(
        row.creator_id,
        best_platform,
        row.content_type,
        current_time,
        activity_map,
        history_map,
        creator_map
    )

    decision = decide_schedule(
        current_time, best_time, current_score, best_score
    )

    results.append([
        row.content_id,
        best_platform,
        best_time,
        decision
    ])

df = pd.DataFrame(results, columns=[
    "content_id", "platform", "time_slot", "decision"
])

df.to_csv("submission.csv", index=False)

print("✅ Done!")