from cybernauts.state import CybernautState
from organs.red_team.routes import get_latest_red_events
from organs.blue_team.routes import get_latest_blue_events
from organs.grey_team.routes import get_latest_grey_events
from math_engine.core import get_last_math_result

state = CybernautState()

def get_organ_status():
    return {
        "red": "online",
        "blue": "online",
        "grey": "online",
        "math_engine": "online",
        "cybernauts": "online"
    }

def get_cybernaut_memory():
    return state.get_recent_memory()

def get_activity_feed():
    return (
        get_latest_red_events() +
        get_latest_blue_events() +
        get_latest_grey_events()
    )[-10:]

def get_math_telemetry():
    return get_last_math_result()

def get_heartbeat():
    return "stable"
