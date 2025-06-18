# app/operation/operations.py

class Operation:

    symbol = '?'

    def perform(self, a: float, b: float) -> float:
       
        raise NotImplementedError("Subclasses must implement the 'perform' method.")

class Addition(Operation):
  
    symbol = '+'
    def perform(self, a: float, b: float) -> float:
        return a + b

class Subtraction(Operation):
    
    symbol = '-'
    def perform(self, a: float, b: float) -> float:
        return a - b

class Multiplication(Operation):
    
    symbol = '*'
    def perform(self, a: float, b: float) -> float:
        return a * b

class Division(Operation):
    
    symbol = '/'
    def perform(self, a: float, b: float) -> float:
        
        try:
            result = a / b
        except ZeroDivisionError:
            raise ValueError("Error: Division by zero is not allowed.")
        return result