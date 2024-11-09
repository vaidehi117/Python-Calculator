# Python-Calculator

## Calculator Operations

This module provides basic arithmetic operations: addition, subtraction, multiplication,
and division. These operations accept two floating-point numbers as input and return the
result as a floating-point number. Additionally, the division function handles division by zero
with an appropriate error message.

**Functions:**
- addition(a: float, b: float) -> float: Adds two numbers.
- subtraction(a: float, b: float) -> float: Subtracts the second number from the first.
- multiplication(a: float, b: float) -> float: Multiplies two numbers.
- division(a: float, b: float) -> float: Divides the first number by the second,raises ValueError for division by zero.
![Alt text](<Screenshot from 2024-11-08 23-30-55.png>)

## Calculator Operations Tests

This file contains a series of unit tests for the basic arithmetic operations (addition, subtraction, multiplication, and division) implemented in the app.operations module. The tests verify the correctness of each operation for various input scenarios, including positive, negative, and edge cases.

**Tests Overview**
Each operation is tested with multiple cases to ensure the functions handle a range of input values. The following test cases are included:

- Basic functionality (e.g., adding/subtracting/multiplying/dividing two positive numbers).
- Negative numbers (testing how the operations behave with negative values).
- Floating-point numbers (testing the operations with decimals).
- Edge cases (e.g., division by zero for division operation).
![Alt text](<Screenshot from 2024-11-08 23-34-17.png>)

## Calculator REPL

REPL (Read-Eval-Print Loop) calculator that allows users to perform basic arithmetic operations
such as addition, subtraction, multiplication, and division. It will continuously prompt the user
for operations and numbers until the user types 'exit' to quit the calculator.

The calculator handles four operations:

- Addition: 'add'
- Subtraction: 'subtract'
- Multiplication: 'multiply'
- Division: 'divide'

The program also validates user input to ensure the correct operation is chosen and that numeric values
are entered. In case of errors like division by zero or non-numeric input, appropriate error messages
are displayed to guide the user.

Exits the calculator upon receiving the command 'exit'.

Example:

> > > calculator()
> > > Welcome to the REPL Calculator!
> > > Type 'exit' to quit.
> > > Choose an operation (add, subtract, multiply, divide): add
> > > Enter the first number: 2
> > > Enter the second number: 3
> > > Result: 5.0
> > > Choose an operation (add, subtract, multiply, divide): exit
> > > Exiting the calculator. Goodbye!

![Alt text](<Screenshot from 2024-11-08 23-41-17.png>)

## Calculator REPL Test Suite

This file contains tests for the REPL (Read-Eval-Print-Loop) implementation of a basic calculator program. The tests are designed using the pytest framework and use the monkeypatch feature to simulate user input and capture output from the calculator application. These tests cover a variety of cases, including positive, edge, and negative test scenarios.

**Functions**
run_calculator_with_input(monkeypatch, inputs)
Simulates user input to the calculator REPL and captures the output.

**Parameters:**
monkeypatch: A pytest fixture that allows us to mock built-in functions like input.
inputs: A list of strings representing the user inputs that will be passed sequentially to the calculator.
Returns:
A string containing the captured output of the calculator REPL.
Description: This helper function allows us to simulate a sequence of inputs to the calculator REPL. It sets up the input function to return the next value from the inputs list on each call, runs the calculator, and captures the printed output.

![Alt text](<Screenshot from 2024-11-08 23-42-16.png>)

