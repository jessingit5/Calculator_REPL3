from app.operation.operations import Operation, Addition, Subtraction, Multiplication, Division
from app.calculation.calculation import Calculation
from app.calculator.history import CalculationHistory

class Calculator:

    def __init__(self):
        self.operations: dict[str, type[Operation]] = self._load_operations()
        self.history = CalculationHistory()

    def _load_operations(self) -> dict[str, type[Operation]]:
        return {
            "add": Addition,
            "subtract": Subtraction,
            "multiply": Multiplication,
            "divide": Division
        }

    def perform_calculation(self, op_name: str, a: float, b: float) -> float:
       
        op_name = op_name.lower()
        if op_name not in self.operations:
            raise ValueError(f"Unknown operation: {op_name}")

        operation_class = self.operations[op_name]
        calculation = Calculation(a, b, operation_class())
        self.history.add_calculation(calculation)
        return calculation.result

    def get_calculation_history(self) -> list[Calculation]:
        return self.history.get_history()

    def clear_history(self):
        self.history.clear_history()