from app.calculation import Calculation

def test_calculation_creation():
  
    calc = Calculation(10, 5, "add", 15)
    assert calc.operand_a == 10
    assert calc.operand_b == 5
    assert calc.operation_name == "add"
    assert calc.result == 15

def test_calculation_repr():
    
    calc = Calculation(10, 5, "add", 15)
    expected_repr = "Calculation(10, 5, 'add', 15)"
    assert repr(calc) == expected_repr