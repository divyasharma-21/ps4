import pandas as pd

def load_data():
    content = pd.read_csv("data/raw/content.csv")
    activity = pd.read_csv("data/raw/platform_activity.csv")
    history = pd.read_csv("data/raw/historical_engagement.csv")
    creators = pd.read_csv("data/raw/creators.csv")

    return content, activity, history, creators
def preprocess(activity, history, creators):
    activity_map = {
        (row.platform, row.time_slot): row.activity_score
        for _, row in activity.iterrows()
    }

    history_map = {
        (row.creator_id, row.platform, row.content_type, row.time_slot): row.avg_engagement
        for _, row in history.iterrows()
    }

    creator_map = {
        row.creator_id: row.base_engagement
        for _, row in creators.iterrows()
    }

    return activity_map, history_map, creator_map