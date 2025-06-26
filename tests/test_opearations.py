import pytest
from app.operations import Operation, OperationFactory, Root

def test_base_operation_not_implemented():

    op = Operation()
    with pytest.raises(NotImplementedError):
        op.execute(1, 2)

@pytest.mark.parametrize("op_name, a, b, expected", [
    ("add", 10, 5, 15), ("subtract", 10, 5, 5), ("multiply", 10, 5, 50),
    ("divide", 10, 2, 5), ("power", 2, 3, 8), ("root", 27, 3, 3),
    ("root", -27, 3, -3)
])
def test_operations(op_name, a, b, expected):

    operation = OperationFactory.create_operation(op_name)
    assert operation.execute(a, b) == expected

def test_division_by_zero():
    div_op = OperationFactory.create_operation("divide")
    with pytest.raises(ValueError, match="Division by zero"):
        div_op.execute(10, 0)

def test_invalid_root():
    root_op = Root()
    with pytest.raises(ValueError, match="even root of a negative number"):
        root_op.execute(-4, 2)

def test_invalid_operation_in_factory():
    with pytest.raises(ValueError, match="Unknown operation: 'log'"):
        OperationFactory.create_operation("log")