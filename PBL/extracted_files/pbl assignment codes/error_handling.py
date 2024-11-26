# Define a custom exception
class CustomError(Exception):
    """Custom exception for specific error conditions."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Function that raises various exceptions
def exception_demo(value, divisor, filename):
    try:
        # Raise ValueError if the value is not an integer
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")
        
        # Raise TypeError if the divisor is not a number
        if not isinstance(divisor, (int, float)):
            raise TypeError("Divisor must be a number.")
        
        # Check for division by zero
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        
        # Perform division
        result = value / divisor
        print(f"Result of division: {result}")
        
        # Attempt to open a file
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of {filename}: {content}")
    
    except ValueError as ve:
        print(f"ValueError occurred: {ve}")
    
    except TypeError as te:
        print(f"TypeError occurred: {te}")
    
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError occurred: {zde}")
    
    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError occurred: {fnfe}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("End of exception handling demo.")

# Raise and handle a custom exception
def raise_custom_exception(condition):
    try:
        if condition:
            raise CustomError("This is a custom exception raised for a specific condition.")
        else:
            print("No custom exception raised.")
    except CustomError as ce:
        print(f"CustomError occurred: {ce}")
    finally:
        print("Custom exception handling complete.")

# Main program
if __name__ == "__main__":
    # Test the exception_demo function with various inputs
    print("### Testing built-in exception handling ###")
    exception_demo("ten", 5, "nonexistent_file.txt")  # Raises ValueError and FileNotFoundError
    exception_demo(10, "five", "example.txt")        # Raises TypeError
    exception_demo(10, 0, "example.txt")             # Raises ZeroDivisionError
    exception_demo(10, 2, "example.txt")             # FileNotFoundError for this example

    print("\n### Testing custom exception ###")
    raise_custom_exception(True)
    raise_custom_exception(False)