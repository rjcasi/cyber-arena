def interpret_red(message):
    return f"Offensive analysis of '{message}' (simulated)."

def interpret_blue(message):
    return f"Defensive interpretation of '{message}' (simulated)."

def interpret_grey(message):
    return f"Automation-oriented interpretation of '{message}' (simulated)."

def interpret_prime(message):
    return f"Holistic symbolic interpretation of '{message}' (simulated)."

profiles = {
    "prime": {
        "name": "Prime Cybernaut",
        "mode": "holistic",
        "interpret": interpret_prime
    },
    "red": {
        "name": "Red Cybernaut",
        "mode": "offensive",
        "interpret": interpret_red
    },
    "blue": {
        "name": "Blue Cybernaut",
        "mode": "defensive",
        "interpret": interpret_blue
    },
    "grey": {
        "name": "Grey Cybernaut",
        "mode": "automation",
        "interpret": interpret_grey
    }
}

def get_profile(name: str):
    return profiles.get(name, profiles["prime"])
