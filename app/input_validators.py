def validate_operands(inputs: list[str]):
    if len(inputs) != 2:
        raise ValueError("Error: Exactly two numbers are required for this operation.")
    try:
        a = float(inputs[0])
        b = float(inputs[1])
        return a, b
    except ValueError:
        raise ValueError("Error: Both inputs must be valid numbers.") from None