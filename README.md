# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
The games purpose at a base level is a number guesing game. However, this projects purpose is how someone working on a project can use AI as a tool to fix bugs in a project and seeing if the code it generates is correct.
- [ ] Detail which bugs you found.
Difficulty was backwards (Normal was Hard and Hard was normal)
Score was off
Hints were off
New Game Button did nothing 
Changing difficulties did not reset the game
Hint range was constatntly 1-100
Entering an empty guess counted against the user

- [ ] Explain what fixes you applied.
Swapped Normal/Hard difficulty ranges — Normal was 1–100 and Hard was 1–50 (backwards). Fixed to Easy: 1–20, Normal: 1–50, Hard: 1–100.
Fixed update_score off-by-one — The win formula had an extra +1 (100 - 10 * (attempt_number + 1)), so a first-attempt win scored 80 instead of 90. Removed the +1.
Fixed Too High giving bonus points — On even attempt numbers, Too High incorrectly awarded +5. Now both Too High and Too Low always deduct 5 points consistently.
Moved game logic from app.py to logic_utils.py — get_range_for_difficulty and parse_guess were relocated here so logic is testable and separated from the UI.
app.py

Fixed "New Game" button doing nothing — The button was not resetting status, score, or history, so the game stayed in a broken state. Now fully resets all session state.
Fixed difficulty change not resetting game — Switching difficulty mid-game didn't reset the secret, attempts, or score. Added a check for st.session_state.difficulty != difficulty to trigger a full reset.
Fixed hint range showing 1–100 always — The st.info prompt hardcoded 1 and 100 instead of using {low} and {high} from the selected difficulty.
Fixed empty/invalid input costing an attempt — The attempt counter incremented even on rejected input. Moved the increment inside the valid-guess branch.
Fixed lexicographic secret comparison bug — On every other turn, secret was cast to str, causing comparisons like 10 > "9" to fail lexicographically. Now always passes secret as int to check_guess.
Rotated attempt limits — Easy had 6, Normal had 8, Hard had 5. Corrected to Easy: 5, Normal: 6, Hard: 8 so harder difficulties actually have fewer attempts.
Fixed starting attempt count — attempts initialized to 1 instead of 0, causing the first guess to display as attempt 2.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess
2. Game returns "Too Low" or "Too high"
3. User enters a new guess
4. Score updates correctly after each guess
5. Game ends after the correct guess or if user loses
6. Enter new game
7. Choose a new difficulty before making a new guess
8. Repeat step 1

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
======================================================================================================================== test session starts ========================================================================================================================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0 -- /Applications/Xcode.app/Contents/Developer/usr/bin/python3
cachedir: .pytest_cache
rootdir: /Users/lorta/Documents/GitHub/ai110-module1show-gameglitchinvestigator-starter
collected 25 items                                                                                                                                                                                                                                                  

test/test_game_logic.py::TestGetRangeForDifficulty::test_easy_range PASSED                                                                                                                                                                                    [  4%]
test/test_game_logic.py::TestGetRangeForDifficulty::test_normal_range PASSED                                                                                                                                                                                  [  8%]
test/test_game_logic.py::TestGetRangeForDifficulty::test_hard_range PASSED                                                                                                                                                                                    [ 12%]
test/test_game_logic.py::TestGetRangeForDifficulty::test_unknown_difficulty_defaults PASSED                                                                                                                                                                   [ 16%]
test/test_game_logic.py::TestGetRangeForDifficulty::test_difficulty_scales_up PASSED                                                                                                                                                                          [ 20%]
test/test_game_logic.py::TestCheckGuess::test_correct_guess PASSED                                                                                                                                                                                            [ 24%]
test/test_game_logic.py::TestCheckGuess::test_too_low PASSED                                                                                                                                                                                                  [ 28%]
test/test_game_logic.py::TestCheckGuess::test_too_high PASSED                                                                                                                                                                                                 [ 32%]
test/test_game_logic.py::TestCheckGuess::test_secret_as_int_not_str PASSED                                                                                                                                                                                    [ 36%]
test/test_game_logic.py::TestCheckGuess::test_boundary_one_above PASSED                                                                                                                                                                                       [ 40%]
test/test_game_logic.py::TestCheckGuess::test_boundary_one_below PASSED                                                                                                                                                                                       [ 44%]
test/test_game_logic.py::TestUpdateScore::test_win_first_attempt PASSED                                                                                                                                                                                       [ 48%]
test/test_game_logic.py::TestUpdateScore::test_win_second_attempt PASSED                                                                                                                                                                                      [ 52%]
test/test_game_logic.py::TestUpdateScore::test_win_minimum_score_floor PASSED                                                                                                                                                                                 [ 56%]
test/test_game_logic.py::TestUpdateScore::test_too_high_deducts_five PASSED                                                                                                                                                                                   [ 60%]
test/test_game_logic.py::TestUpdateScore::test_too_high_odd_attempt_deducts_five PASSED                                                                                                                                                                       [ 64%]
test/test_game_logic.py::TestUpdateScore::test_too_low_deducts_five PASSED                                                                                                                                                                                    [ 68%]
test/test_game_logic.py::TestUpdateScore::test_unknown_outcome_no_change PASSED                                                                                                                                                                               [ 72%]
test/test_game_logic.py::TestUpdateScore::test_score_accumulates PASSED                                                                                                                                                                                       [ 76%]
test/test_game_logic.py::TestParseGuess::test_valid_integer PASSED                                                                                                                                                                                            [ 80%]
test/test_game_logic.py::TestParseGuess::test_empty_string PASSED                                                                                                                                                                                             [ 84%]
test/test_game_logic.py::TestParseGuess::test_none_input PASSED                                                                                                                                                                                               [ 88%]
test/test_game_logic.py::TestParseGuess::test_non_numeric PASSED                                                                                                                                                                                              [ 92%]
test/test_game_logic.py::TestParseGuess::test_float_string_truncates PASSED                                                                                                                                                                                   [ 96%]
test/test_game_logic.py::TestParseGuess::test_invalid_guess_does_not_cost_attempt PASSED   

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
