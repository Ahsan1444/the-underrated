import sys

def color_text(color): # Made a Decorator Manual function to change text color in terminal output
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "yellow": "\033[93m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
    }

    def decorator(func):  # Define the decorator function that wraps another function
        def wrapper(*args, **kwargs): 
            result = func(*args, **kwargs)  
            if sys.stdout.isatty():
                return f"{colors[color]}{result}{colors['reset']}"  # Apply color formatting for terminal output
            else:
                return result
        return wrapper 
    return decorator 