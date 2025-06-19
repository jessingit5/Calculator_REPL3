from ..calculation import Calculation

class CalculationHistory:
    _history: list[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls._history.append(calculation)

    @classmethod
    def get_history(cls) -> list[Calculation]:
        return cls._history

    @classmethod
    def clear_history(cls):
        cls._history.clear()