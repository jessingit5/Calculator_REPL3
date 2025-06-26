import pytest
from app.input_validators import validate_operands

def test_validate_operands_valid():
 
    assert validate_operands(["5", "10.5"]) == (5.0, 10.5)

@pytest.mark.parametrize("inputs, expected_error", [
    (["5"], "Exactly two numbers are required"),
    (["5", "10", "15"], "Exactly two numbers are required"),
    (["a", "10"], "Both inputs must be valid numbers"),
    (["5", "b"], "Both inputs must be valid numbers"),
])
def test_validate_operands_invalid(inputs, expected_error):

    with pytest.raises(ValueError, match=expected_error):
        validate_operands(inputs)