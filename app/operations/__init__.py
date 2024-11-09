def addition(a: float, b: float) -> float:
    """
    Returns:
    float: The result of adding `a` and `b`.
    """
    return a + b

def subtraction(a: float, b: float) -> float:
    """
    Returns:
    float: The result of subtracting `b` from `a`.
    """
    return a - b

def multiplication(a: float, b: float) -> float:
    """
    Returns:
    float: The result of multiplying `a` by `b`.
    """
    return a * b 

def division(a: float, b: float) -> float:
    """
    Returns:
    float: The result of dividing `a` by `b`.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")  # Guard against division by zero
    return a / b
