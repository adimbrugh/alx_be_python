
def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator
        return f"Result: {result}"
    
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    except ValueError:
        return "Error: Non-numeric input provided. Please valid numbers."