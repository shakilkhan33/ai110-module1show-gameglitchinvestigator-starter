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

- [x] Describe the game's purpose.
   - The game is a simple number guessing game where the player tries to guess a secret number, receiving hints after each guess.
- [x] Detail which bugs you found.
   - The secret number changes every time the user submits a guess, making it impossible to win.
   - The hints for "Higher" or "Lower" are incorrect and do not reflect the actual relationship between the guess and the secret number.
- [x] Explain what fixes you applied.
   - Used Streamlit's session state to persist the secret number between guesses so it doesn't reset.
   - Corrected the logic for the hints so that they accurately tell the player if their guess is too high or too low.

## 📸 Demo

- [ ] ![Here is the screenshots, I have done so far](./Images/Screenshot%202026-03-16%20000213.png)
[ ] ![Here is the screenshots, I have done so far](./Images/Screenshot%202026-03-16%20000249.png)
[ ] ![Here is the screenshots, I have done so far](./Images/Screenshot%202026-03-16%20000325.png)
[ ] ![Here is the screenshots, I have done so far](./Images/Screenshot%202026-03-16%20000411.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
