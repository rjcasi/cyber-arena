def analyze_embedding(text: str):
    length = len(text.split())
    return (
        f"[Embedding Engine]\n"
        f"Input: {text}\n"
        f"Token count: {length}\n"
        f"Simulated embedding vector: [{', '.join(['0.1']*min(8, length))}]\n"
    )
