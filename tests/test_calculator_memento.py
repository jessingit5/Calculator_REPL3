import pytest
import pandas as pd
from app.calculator_memento import Memento, Caretaker

@pytest.fixture
def caretaker():
    return Caretaker()

@pytest.fixture
def mementos():
    return [
        Memento(pd.DataFrame({'A': []})),
        Memento(pd.DataFrame({'A': [1]})),
        Memento(pd.DataFrame({'A': [1, 2]}))
    ]

def test_caretaker_save(caretaker, mementos):
    caretaker.save_state(mementos[0])
    caretaker.save_state(mementos[1])
    assert len(caretaker._undo_mementos) == 2

def test_caretaker_undo(caretaker, mementos):
    caretaker.save_state(mementos[0])
    caretaker.save_state(mementos[1])
    caretaker.save_state(mementos[2])
    restored = caretaker.undo()
    pd.testing.assert_frame_equal(restored.get_state(), mementos[1].get_state())
    assert len(caretaker._undo_mementos) == 2
    assert len(caretaker._redo_mementos) == 1

def test_caretaker_redo(caretaker, mementos):
    caretaker.save_state(mementos[0])
    caretaker.save_state(mementos[1])
    caretaker.save_state(mementos[2])
    caretaker.undo()
    restored = caretaker.redo()
    pd.testing.assert_frame_equal(restored.get_state(), mementos[2].get_state())
    assert len(caretaker._undo_mementos) == 3
    assert len(caretaker._redo_mementos) == 0

def test_undo_at_limit(caretaker, mementos):
    caretaker.save_state(mementos[0])
    with pytest.raises(IndexError, match="Cannot undo"):
        caretaker.undo()

def test_redo_at_limit(caretaker):
    with pytest.raises(IndexError, match="Cannot redo"):
        caretaker.redo()

def test_save_clears_redo_stack(caretaker, mementos):
    caretaker.save_state(mementos[0])
    caretaker.save_state(mementos[1])
    caretaker.undo()
    assert len(caretaker._redo_mementos) == 1
    caretaker.save_state(mementos[2])
    assert len(caretaker._redo_mementos) == 0