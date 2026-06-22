import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


# --- get_range_for_difficulty ---
# FIX: Normal and Hard ranges were swapped; Easy/Normal/Hard should scale up

class TestGetRangeForDifficulty:
    def test_easy_range(self):
        assert get_range_for_difficulty("Easy") == (1, 20)

    def test_normal_range(self):
        # Was (1, 100) before the fix — must be (1, 50)
        assert get_range_for_difficulty("Normal") == (1, 50)

    def test_hard_range(self):
        # Was (1, 50) before the fix — must be (1, 100)
        assert get_range_for_difficulty("Hard") == (1, 100)

    def test_unknown_difficulty_defaults(self):
        assert get_range_for_difficulty("Unknown") == (1, 100)

    def test_difficulty_scales_up(self):
        _, easy_high = get_range_for_difficulty("Easy")
        _, normal_high = get_range_for_difficulty("Normal")
        _, hard_high = get_range_for_difficulty("Hard")
        assert easy_high < normal_high < hard_high


# --- check_guess ---
# FIX: secret was sometimes passed as str causing lexicographic comparison

class TestCheckGuess:
    def test_correct_guess(self):
        outcome, _ = check_guess(42, 42)
        assert outcome == "Win"

    def test_too_low(self):
        outcome, _ = check_guess(10, 50)
        assert outcome == "Too Low"

    def test_too_high(self):
        outcome, _ = check_guess(90, 50)
        assert outcome == "Too High"

    def test_secret_as_int_not_str(self):
        # Before the fix, secret could be str("9") and guess int(10).
        # "10" < "9" lexicographically, so check_guess would wrongly return Too High.
        outcome, _ = check_guess(10, 9)
        assert outcome == "Too High"

    def test_boundary_one_above(self):
        outcome, _ = check_guess(21, 20)
        assert outcome == "Too High"

    def test_boundary_one_below(self):
        outcome, _ = check_guess(19, 20)
        assert outcome == "Too Low"


# --- update_score ---
# FIX 1: attempt_number was off-by-one (+1 extra), so first-attempt win scored 80 not 90
# FIX 2: "Too High" no longer gives +5 on even attempts — both wrong directions cost -5

class TestUpdateScore:
    def test_win_first_attempt(self):
        # attempt_number=1 → 100 - 10*1 = 90
        assert update_score(0, "Win", 1) == 90

    def test_win_second_attempt(self):
        # attempt_number=2 → 100 - 10*2 = 80
        assert update_score(0, "Win", 2) == 80

    def test_win_minimum_score_floor(self):
        # attempt_number=10 → 100 - 100 = 0, clamped to 10
        assert update_score(0, "Win", 10) == 10

    def test_too_high_deducts_five(self):
        # Before fix, even attempt numbers incorrectly awarded +5
        assert update_score(50, "Too High", 2) == 45

    def test_too_high_odd_attempt_deducts_five(self):
        assert update_score(50, "Too High", 3) == 45

    def test_too_low_deducts_five(self):
        assert update_score(50, "Too Low", 1) == 45

    def test_unknown_outcome_no_change(self):
        assert update_score(50, "SomeOtherOutcome", 1) == 50

    def test_score_accumulates(self):
        score = 0
        score = update_score(score, "Too Low", 1)   # -5 → 45 from 50? start at 0 → -5
        score = update_score(score, "Win", 2)        # +80
        assert score == 75


# --- parse_guess ---

class TestParseGuess:
    def test_valid_integer(self):
        ok, val, _ = parse_guess("42")
        assert ok and val == 42

    def test_empty_string(self):
        ok, val, _ = parse_guess("")
        assert not ok and val is None

    def test_none_input(self):
        ok, val, _ = parse_guess(None)
        assert not ok and val is None

    def test_non_numeric(self):
        ok, _, _ = parse_guess("abc")
        assert not ok

    def test_float_string_truncates(self):
        ok, val, _ = parse_guess("7.9")
        assert ok and val == 7

    def test_invalid_guess_does_not_cost_attempt(self):
        # parse_guess returning ok=False means the caller should skip incrementing attempts
        ok, _, _ = parse_guess("not a number")
        assert ok is False
