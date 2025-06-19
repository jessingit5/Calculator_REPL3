
from ..operation.operations import Operation

class Calculation:
    
    
    def __init__(self, a: float, b: float, operation: Operation):
      
        self.a = a
        self.b = b
        self.operation = operation
        self.result = self.operation.perform(self.a, self.b)

    def __repr__(self) -> str:
        
        op_symbol = self.operation.symbol
        return f"{self.a} {op_symbol} {self.b} = {self.result}"