class CybernautState:
    def __init__(self):
        self.memory = []

    def update_memory(self, message: str):
        self.memory.append(message)
        if len(self.memory) > 20:
            self.memory.pop(0)


def get_recent_memory(self, n=5):
    return self.memory[-n:]
