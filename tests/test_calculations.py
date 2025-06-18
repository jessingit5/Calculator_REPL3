import pytest
from app.calculation.calculation import Calculation
from app.operation.operations import Addition, Subtraction, Multiplication, Division

@pytest.mark.parametrize("a, b, operation, expected_result, expected_repr", [
    (10, 5, Addition(), 15, "10.0 + 5.0 = 15.0"),
    (20, 3, Subtraction(), 17, "20.0 - 3.0 = 17.0"),
    (4, 5, Multiplication(), 20, "4.0 * 5.0 = 20.0"),
    (10, 2, Division(), 5, "10.0 / 2.0 = 5.0"),
    (10, 0, Division(), None, None)
])
def test_calculation(a, b, operation, expected_result, expected_repr):
    if b == 0 and isinstance(operation, Division):
        with pytest.raises(ValueError):
            Calculation(a, b, operation)
    else:
        calc = Calculation(a, b, operation)
        assert calc.result == expected_result
        assert repr(calc) == expected_repr

def test_calculation_repr_unknown_op():
    class MockOperation:
        def perform(self, a, b):
            return a ** b
        
    calc = Calculation(2, 3, MockOperation())
    assert repr(calc) == "2.0 ? 3.0 = 8.0"