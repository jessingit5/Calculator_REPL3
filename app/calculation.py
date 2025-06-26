class Calculation:
    def __init__(self, operand_a: float, operand_b: float, operation_name: str, result: float):
        self.operand_a = operand_a
        self.operand_b = operand_b
        self.operation_name = operation_name
        self.result = result

    def __repr__(self):
        return f"Calculation({self.operand_a}, {self.operand_b}, '{self.operation_name}', {self.result})"