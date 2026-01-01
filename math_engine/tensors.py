def parse_vector(text):
    return [float(x.strip()) for x in text.split(",")]

def analyze_tensor(text: str):
    vec = parse_vector(text)
    magnitude = sum(x*x for x in vec) ** 0.5

    return (
        f"[Tensor Analysis]\n"
        f"Vector: {vec}\n"
        f"Dimension: {len(vec)}\n"
        f"Magnitude: {magnitude:.4f}\n"
        f"Normalized: {[round(x/magnitude, 4) for x in vec]}\n"
    )
