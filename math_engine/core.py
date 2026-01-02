from .number_theory import analyze_number
from .tensors import analyze_tensor
from .physics import analyze_physics
from .embeddings import analyze_embedding

# Telemetry: store the last computation result
last_math_result = "No computations yet."

def get_last_math_result():
    """
    Returns the last computed math result as a string.
    Used by the Prime Cockpit telemetry layer.
    """
    return last_math_result


def process_math(query: str):
    """
    Central dispatch for the Math Engine.
    Routes the query to number theory, tensor analysis,
    physics, or embeddings based on simple heuristics.
    """
    global last_math_result

    if not query:
        last_math_result = "No input provided."
        return last_math_result

    # Simple routing logic (you can evolve this later)
    if query.isdigit():
        last_math_result = analyze_number(int(query))

    elif "," in query:
        # Interpret comma-separated values as a vector
        last_math_result = analyze_tensor(query)

    elif "energy" in query.lower() or "mass" in query.lower():
        last_math_result = analyze_physics(query)

    else:
        # Fallback to embedding-style symbolic analysis
        last_math_result = analyze_embedding(query)

    return last_math_result
