from .state import CybernautState

class PrimeCybernaut:
    def __init__(self):
        self.state = CybernautState()

    def process(self, message: str, profile):
        if not message:
            return "No input provided."

        # Symbolic reasoning (simulated)
        tokens = message.split()
        token_count = len(tokens)

        self.state.update_memory(message)

        return (
            f"[Prime Cybernaut]\n"
            f"Profile: {profile['name']}\n"
            f"Message received: {message}\n"
            f"Token count: {token_count}\n"
            f"Symbolic mode: {profile['mode']}\n"
            f"Interpretation: {profile['interpret'](message)}\n"
            f"Memory size: {len(self.state.memory)} entries\n"
        )
