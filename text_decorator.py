def color_text(color):
    """Decorator to change text color in terminal output AND files."""
    colors = {
        "red": "\033[91m", 
        "green": "\033[92m", 
        "blue": "\033[94m", 
        "reset": "\033[0m"
    }

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{colors[color]}{result}{colors['reset']}"  # Applies color even when saved to file
        return wrapper
    return decorator
