import pandas as pd

class Memento:
   
    def __init__(self, state: pd.DataFrame):
        self._state = state.copy(deep=True)
    def get_state(self) -> pd.DataFrame:
        return self._state

class Caretaker:

    def __init__(self):
        self._undo_mementos: list[Memento] = []
        self._redo_mementos: list[Memento] = []

    def save_state(self, memento: Memento):
        self._undo_mementos.append(memento)
        self._redo_mementos.clear()

    def undo(self) -> Memento:
        if len(self._undo_mementos) <= 1:
            raise IndexError("Cannot undo: No previous state available.")
        current_memento = self._undo_mementos.pop()
        self._redo_mementos.append(current_memento)
        return self._undo_mementos[-1]

    def redo(self) -> Memento:
        if not self._redo_mementos:
            raise IndexError("Cannot redo: No future state available.")
        memento_to_restore = self._redo_mementos.pop()
        self._undo_mementos.append(memento_to_restore)
        return memento_to_restore