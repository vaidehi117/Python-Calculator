import pytest
from app.history import History

def test_add_calculation():
    """Test adding a single calculation to history."""
    history = History()
    history.add_calculation("add 2 3 = 5")
    assert history.get_history() == ["add 2 3 = 5"]

def test_add_multiple_calculations():
    """Test adding multiple calculations to history."""
    history = History()
    calculations = ["add 2 3 = 5", "subtract 5 2 = 3", "multiply 2 3 = 6"]
    for calc in calculations:
        history.add_calculation(calc)
    assert history.get_history() == calculations

def test_clear_history():
    """Test clearing the history after adding calculations."""
    history = History()
    history.add_calculation("add 2 3 = 5")
    history.clear_history()
    assert history.get_history() == []

def test_undo_last():
    """Test undoing the last calculation."""
    history = History()
    history.add_calculation("add 2 3 = 5")
    history.add_calculation("subtract 5 2 = 3")
    history.undo_last()
    assert history.get_history() == ["add 2 3 = 5"]

def test_undo_last_empty_history(capsys):
    """Test undoing the last calculation when history is empty."""
    history = History()
    history.undo_last()
    captured = capsys.readouterr()  # Capture printed output
    assert captured.out.strip() == "History is already empty."
    assert history.get_history() == []

def test_get_history():
    """Test retrieving the history of calculations."""
    history = History()
    calculations = ["add 2 3 = 5", "multiply 4 5 = 20"]
    for calc in calculations:
        history.add_calculation(calc)
    assert history.get_history() == calculations

def test_clear_history_empty():
    """Test clearing history when it is already empty."""
    history = History()
    history.clear_history()
    assert history.get_history() == []

def test_add_non_string_calculation():
    """Test adding a non-string calculation."""
    history = History()
    with pytest.raises(TypeError):
        history.add_calculation(12345)  # Should raise TypeError

def test_add_calculation_none():
    """Test adding None as a calculation."""
    history = History()
    with pytest.raises(TypeError):
        history.add_calculation(None)  # Should raise TypeError

def test_get_history_is_copy():
    """Test that get_history returns a copy, not a reference."""
    history = History()
    history.add_calculation("add 1 1 = 2")
    retrieved_history = history.get_history()
    retrieved_history.append("subtract 2 1 = 1")
    # The original history should not be modified
    assert history.get_history() == ["add 1 1 = 2"]

def test_undo_last_after_clear(capsys):
    """Test undoing the last calculation after clearing the history."""
    history = History()
    history.add_calculation("add 2 3 = 5")
    history.clear_history()
    history.undo_last()
    captured = capsys.readouterr()  # Capture printed output
    assert captured.out.strip() == "History is already empty."
    assert history.get_history() == []