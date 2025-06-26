
import math

class Operation:
    def execute(self, a: float, b: float) -> float:
        raise NotImplementedError("Subclasses must implement the 'execute' method.")

class Addition(Operation):
    def execute(self, a: float, b: float) -> float: return a + b

class Subtraction(Operation):
    def execute(self, a: float, b: float) -> float: return a - b

class Multiplication(Operation):
    def execute(self, a: float, b: float) -> float: return a * b

class Division(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Error: Division by zero is not allowed.")
        return a / b

class Power(Operation):
    def execute(self, a: float, b: float) -> float: return math.pow(a, b)

class Root(Operation):
    def execute(self, a: float, b: float) -> float:
        if a < 0 and b % 2 == 0:
            raise ValueError("Error: Cannot take an even root of a negative number.")
        return -math.pow(abs(a), 1/b) if a < 0 else math.pow(a, 1/b)

class OperationFactory:
    _operations = {
        "add": Addition, "subtract": Subtraction, "multiply": Multiplication,
        "divide": Division, "power": Power, "root": Root
    }
    @staticmethod
    def create_operation(op_name: str) -> Operation:
        op_name = op_name.lower()
        if op_name not in OperationFactory._operations:
            raise ValueError(f"Unknown operation: '{op_name}'")
        return OperationFactory._operations[op_name]()