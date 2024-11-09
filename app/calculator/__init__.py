from app.operations import addition, subtraction, multiplication, division

def calculator():
    """
    REPL calculator that performs addition, subtraction, multiplication, and division.
    Continues until the user types 'exit'.
    """
    print("Welcome to the REPL Calculator!")
    print("Type 'exit' to quit.")
    
    while True:
        # Prompt the user to enter an operation
        operation = input("Choose an operation (add, subtract, multiply, divide): ").strip().lower()
        
        # Exit condition
        if operation == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        
        # Check if the operation is valid
        if operation not in ["add", "subtract", "multiply", "divide"]:
            # Inform the user of the unknown operation and available options
            print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
            continue
        
        # Get user input for the two numbers
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter numeric values.")
            continue
        
        # Perform the selected operation and handle exceptions if any
        try:
            if operation == "add":
                result = addition(a, b)
            elif operation == "subtract":
                result = subtraction(a, b)
            elif operation == "multiply":
                result = multiplication(a, b)
            elif operation == "divide":
                result = division(a, b)
            
            # Print the result
            print(f"Result: {result}")
        
        except ValueError as e:
            # Handle division by zero error
            print(e)

# Run the calculator if this file is executed directly
# if __name__ == "__main__":
#     calculator()