
import os

class CalculatorConfig:

    def __init__(self):
        self.history_file_path = self._get_env_variable('HISTORY_FILE_PATH')

    def _get_env_variable(self, var_name: str) -> str:

        value = os.getenv(var_name)
        if not value:
            raise ValueError(f"Configuration error: Environment variable '{var_name}' not set.")
        return value