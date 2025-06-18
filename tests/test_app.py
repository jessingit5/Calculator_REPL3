import pytest
from unittest.mock import patch
from app.calculator import Calculator
from app.__main__ import App

@pytest.fixture
def app_instance():
    app = App()
    app.calculator.clear_history()
    return app

@patch('builtins.input')
def test_app_exit_command(mock_input, capsys, app_instance):
    mock_input.side_effect = ['exit']
    with pytest.raises(SystemExit):
        app_instance.start()
    captured = capsys.readouterr()
    assert "Exiting calculator. Goodbye!" in captured.out

@patch('builtins.input')
def test_app_help_command(mock_input, capsys, app_instance):
    mock_input.side_effect = ['help', 'exit']
    with pytest.raises(SystemExit):
        app_instance.start()
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out

@patch('builtins.input')
def test_app_history_command(mock_input, capsys, app_instance):
    mock_input.side_effect = [
        'history',
        'add', '5', '3',
        'history', 
        'exit'
    ]
    with pytest.raises(SystemExit):
        app_instance.start()
    captured = capsys.readouterr()
    assert "No calculations in history yet." in captured.out
    assert "Result: 8.0" in captured.out
    assert "Calculation History:" in captured.out
    assert "5.0 + 3.0 = 8.0" in captured.out

@patch('builtins.input')
def test_app_unknown_command(mock_input, capsys, app_instance):
    mock_input.side_effect = ['fly', 'exit']
    with pytest.raises(SystemExit):
        app_instance.start()
    captured = capsys.readouterr()
    assert "Unknown command: 'fly'" in captured.out

@patch('builtins.input')
def test_app_invalid_number_input(mock_input, capsys, app_instance):
    mock_input.side_effect = ['add', 'five', '3', '5', '3', 'exit']
    with pytest.raises(SystemExit):
        app_instance.start()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter valid numbers." in captured.out
    assert "Result: 8.0" in captured.out

@patch('builtins.input')
def test_app_division_by_zero(mock_input, capsys, app_instance):
    mock_input.side_effect = ['divide', '10', '0', 'exit']
    with pytest.raises(SystemExit):
        app_instance.start()
    captured = capsys.readouterr()
    assert "Error: Division by zero is not allowed." in captured.out