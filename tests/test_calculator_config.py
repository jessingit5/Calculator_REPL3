import pytest
from unittest.mock import patch
from app.calculator_config import CalculatorConfig

def test_config_load_success():

    with patch('os.getenv', return_value='test_history.csv') as mock_getenv:
        config = CalculatorConfig()
        mock_getenv.assert_called_once_with('HISTORY_FILE_PATH')
        assert config.history_file_path == 'test_history.csv'

def test_config_load_failure():

    with patch('os.getenv', return_value=None):
        with pytest.raises(ValueError, match="Configuration error: Environment variable 'HISTORY_FILE_PATH' not set."):
            CalculatorConfig()