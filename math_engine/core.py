from .number_theory import analyze_number
from .tensors import analyze_tensor
from .physics import analyze_physics
from .embeddings import analyze_embedding

def process_math(query: str):
    if not query:
        return "No input provided."

    # Simple routing logic (simulated)
    if query.isdigit():
        return analyze_number(int(query))

    if "," in query:
        return analyze_tensor(query)

    if "energy" in query.lower() or "mass" in query.lower():
        return analyze_physics(query)

    return analyze_embedding(query)
