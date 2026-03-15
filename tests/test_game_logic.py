import types
from logic_utils import reset_game_session_state

def test_reset_game_session_state_resets_all_fields():
    # Simulate a session_state object
    session_state = types.SimpleNamespace()
    session_state.attempts = 5
    session_state.secret = 42
    session_state.status = "won"
    session_state.history = [1, 2, 3]
    session_state.score = 99
    # Call reset
    reset_game_session_state(session_state, low=10, high=20)
    # Check all fields are reset
    assert session_state.attempts == 0
    assert 10 <= session_state.secret <= 20
    assert session_state.status == "playing"
    assert session_state.history == []
    assert session_state.score == 0
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic_utils import check_guess

def test_check_guess_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_check_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_check_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_check_guess_win_str():
    # Handles TypeError branch: secret as string
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"
    assert "Correct" in message

def test_check_guess_too_high_str():
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert "LOWER" in message

def test_check_guess_too_low_str():
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"
    assert "HIGHER" in message
