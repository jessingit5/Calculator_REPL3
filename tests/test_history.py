import pandas as pd
from pandas.testing import assert_frame_equal
from app.history import HistoryManager
from app.calculation import Calculation

def test_add_record():
    manager = HistoryManager()
    calc = Calculation(10, 5, "add", 15)
    manager.add_record(calc)
    df = manager.get_history()
    assert len(df) == 1
    assert df.iloc[0]["Operation"] == "add"

def test_clear_history():
    manager = HistoryManager()
    manager.add_record(Calculation(10, 5, "add", 15))
    manager.clear()
    assert manager.get_history().empty

def test_set_history():
    manager = HistoryManager()
    new_df = pd.DataFrame({'A': [1], 'B': [2]})
    manager.set_history(new_df)
    assert_frame_equal(manager.get_history(), new_df)

    new_df['A'] = 5
    assert not manager.get_history().equals(new_df)

def test_save_and_load_csv(tmp_path):
    manager1 = HistoryManager()
    manager1.add_record(Calculation(20, 10, "subtract", 10))
    file_path = tmp_path / "history.csv"
    manager1.save_to_csv(file_path)

    manager2 = HistoryManager()
    manager2.load_from_csv(file_path)
    assert_frame_equal(manager1.get_history(), manager2.get_history())

def test_load_nonexistent_file(capsys):
    manager = HistoryManager()
    manager.load_from_csv("nonexistent_file.csv")
    captured = capsys.readouterr()
    assert "No history file found" in captured.out
    assert manager.get_history().empty

def test_save_io_error(capsys):
    manager = HistoryManager()
    with patch("builtins.open", side_effect=IOError("Permission denied")):
        manager.save_to_csv("/unwritable/path/history.csv")
        captured = capsys.readouterr()
        assert "Error saving history" in captured.out

def test_load_generic_error(capsys):
    manager = HistoryManager()
    with patch("pandas.read_csv", side_effect=Exception("Corrupted file")):
        manager.load_from_csv("dummy.csv")
        captured = capsys.readouterr()
        assert "Error loading history" in captured.out