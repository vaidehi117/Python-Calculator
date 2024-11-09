import sys
from io import StringIO
import pytest
from app.calculator import calculator  # Assuming your REPL code is in `operations_repl.py`

def run_calculator_with_input(monkeypatch, inputs):
  
    # Simulate user inputs in sequence
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Capture output from the calculator
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()  # Run the calculator REPL
    sys.stdout = sys.__stdout__  # Reset stdout to original
    return captured_output.getvalue()

# Positive Tests
def test_addition(monkeypatch):
    """Test addition operation in REPL."""
    inputs = ["add", "2", "3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output

def test_subtraction(monkeypatch):
    """Test subtraction operation in REPL."""
    inputs = ["subtract", "5", "2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 3.0" in output

def test_multiplication(monkeypatch):
    """Test multiplication operation in REPL."""
    inputs = ["multiply", "4", "5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 20.0" in output

def test_division(monkeypatch):
    """Test division operation in REPL."""
    inputs = ["divide", "10", "2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output

# Edge Case and Negative Tests
def test_division_by_zero(monkeypatch):
    """Test division by zero in REPL."""
    inputs = ["divide", "10", "0", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Division by zero is not allowed." in output

def test_invalid_operation(monkeypatch):
    """Test invalid operation input in REPL."""
    inputs = ["modulus", "10", "3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Unknown operation 'modulus'. Supported operations: add, subtract, multiply, divide." in output

def test_non_numeric_input(monkeypatch):
    """Test non-numeric input handling in REPL."""
    inputs = ["add", "ten", "5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid input. Please enter numeric values." in output

def test_exit(monkeypatch):
    """Test exiting the REPL."""
    inputs = ["exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Exiting the calculator. Goodbye!" in output
