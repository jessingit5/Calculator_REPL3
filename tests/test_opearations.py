# tests/test_operations.py

import pytest
from app.operation.operations import Addition, Subtraction, Multiplication, Division, Operation

def test_base_operation_not_implemented():
    op = Operation()
    with pytest.raises(NotImplementedError, match="Subclasses must implement the 'perform' method."):
        op.perform(1, 2)

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),  
    (-1, 1, 0),     
    (-5, -5, -10),    
    (1.5, 2.5, 4.0),  
    (0, 0, 0)   
])
def test_addition(a, b, expected):
    
    calc = Addition()
    assert calc.perform(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (-1, 1, -2),
    (5, 10, -5),
    (2.5, 1.5, 1.0),
    (0, 0, 0)
])
def test_subtraction(a, b, expected):

    calc = Subtraction()
    assert calc.perform(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50),
    (-1, 1, -1),
    (-5, -5, 25),
    (1.5, 2.0, 3.0),
    (10, 0, 0)
])
def test_multiplication(a, b, expected):

    calc = Multiplication()
    assert calc.perform(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (-10, 2, -5),
    (5, 2, 2.5),
    (0, 5, 0)
])
def test_division(a, b, expected):
    calc = Division()
    assert calc.perform(a, b) == expected

def test_division_by_zero():
    """Test that division by zero raises a ValueError."""
    calc = Division()
    with pytest.raises(ValueError, match="Error: Division by zero is not allowed."):
        calc.perform(10, 0)