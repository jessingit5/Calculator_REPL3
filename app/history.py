import pandas as pd
from app.calculation import Calculation

class HistoryManager:

    def __init__(self):
        self.history_df = pd.DataFrame(columns=["Operand A", "Operand B", "Operation", "Result"])

    def add_record(self, calculation: Calculation):
        new_record_data = {
            'Operand A': [calculation.operand_a],
            'Operand B': [calculation.operand_b],
            'Operation': [calculation.operation_name],
            'Result': [calculation.result]
        }
        new_record = pd.DataFrame(new_record_data)
        self.history_df = pd.concat([self.history_df, new_record], ignore_index=True)

    def get_history(self) -> pd.DataFrame:
        return self.history_df.copy()

    def set_history(self, df: pd.DataFrame):
        self.history_df = df.copy(deep=True)

    def clear(self):
        self.history_df = self.history_df.iloc[0:0]

    def save_to_csv(self, file_path: str):
        try:
            self.history_df.to_csv(file_path, index=False)
            print(f"History saved to {file_path}")
        except IOError as e:
            print(f"Error saving history: {e}")

    def load_from_csv(self, file_path: str):
        try:
            self.history_df = pd.read_csv(file_path)
            print(f"History loaded from {file_path}")
        except FileNotFoundError:
            print(f"No history file found at {file_path}. Starting fresh.")
        except Exception as e:
            print(f"Error loading history: {e}")