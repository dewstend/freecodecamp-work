def floor_to_base(x, base=10):
    if x > base:
        return round(x - (x % base))
    return 0


def generate_whitespace_chart(width: int, height: int):
    return [[" "] * width for _ in range(height)]
