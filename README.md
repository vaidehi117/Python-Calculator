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

## Calculator Operations Tests
This file contains a series of unit tests for the basic arithmetic operations (addition, subtraction, multiplication, and division) implemented in the app.operations module. The tests verify the correctness of each operation for various input scenarios, including positive, negative, and edge cases.

**Tests Overview**
Each operation is tested with multiple cases to ensure the functions handle a range of input values. The following test cases are included:

- Basic functionality (e.g., adding/subtracting/multiplying/dividing two positive numbers).
- Negative numbers (testing how the operations behave with negative values).
- Floating-point numbers (testing the operations with decimals).
- Edge cases (e.g., division by zero for division operation).
