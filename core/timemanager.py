from datetime import datetime

def current_time():
    return datetime.now().hour

def get_timeperiod():
    hour = current_time()
    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 18:
        return "afternoon"
    elif 18 <= hour < 24:
        return "evening"
    else:
        return "night"