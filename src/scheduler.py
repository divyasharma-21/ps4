def decide_schedule(current_time, best_time, current_score, best_score):
    
    if best_time == current_time:
        return "POST_NOW"

    if best_score > current_score * 1.1:
        return "SCHEDULE"
    
    return "POST_NOW"