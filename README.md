# 🎮 Tic Tac Toe — Python CLI Game

A fully interactive two-player Tic Tac Toe game running in the terminal,
built in Python using object-oriented programming.

![demo](assets/demo.gif)

---

## ✨ Features

- Two-player mode (Player X vs Player O)
- Live board display that updates after each move
- Input validation — rejects invalid or already-taken squares
- Automatic win detection for rows, columns and diagonals
- Draw detection when the board is full
- Play again prompt at the end of each game

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher

### Installation

git clone https://github.com/yourusername/tictactoe-python.git
cd tictactoe-python

### Run the game

python main.py

---

## 🕹 How to Play

Players take turns entering a number from 1–9 corresponding
to a position on the board:

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

The first player to get three in a row (horizontally,
vertically or diagonally) wins. If all squares are filled
with no winner, the game ends in a draw.

---

## 🛠 Built With

- Python 3.11
- Standard library only (no external dependencies)

---

## 📚 What I Learned

- Structuring a project using Object-Oriented Programming
- Handling and validating user input robustly
- Using nested lists to represent a 2D game board
- Writing clean game loop logic with clear win/draw conditions
- Setting up a professional GitHub repository from scratch

---

## 🗺 Future Improvements

- [ ] Add a single-player mode with a basic AI opponent
- [ ] Add score tracking across multiple rounds
- [ ] Add colour to the terminal output using colorama
- [ ] Build a simple GUI version using tkinter

---

## 📄 Licence

This project is licensed under the MIT Licence.
See the [LICENSE](LICENSE) file for details.

---

*Built as Month 1 milestone project while learning Python — part of a
12-month development roadmap.*
```

The **Future Improvements** section with checkboxes is particularly smart — it shows you think ahead, and as you actually add those features you can tick them off and commit the update.

---

## Step 5 — Add a Demo GIF (Big Visual Impact)

This single thing separates good repos from great ones. A GIF of your game actually running takes 2 minutes to make and makes your README look professional immediately.

How to record it:

- On Windows, download **ScreenToGif** (free, google it) — open it, drag the recording frame over your terminal, play your game, stop recording, export as GIF
- On Mac, use **Kap** (free) — same process

Save the file as `demo.gif` inside your `assets/` folder. The line `![demo](assets/demo.gif)` in your README will automatically display it on GitHub. When someone opens your repo they'll see the game running before they read a single word.

---

## Step 6 — Configure the Repo's About Section on GitHub

On your repo's main page on GitHub, click the **gear icon** next to "About" on the right side. Fill in:

- **Description:** same one-liner as your repo description
- **Website:** leave blank for now
- **Topics:** add these tags: `python`, `game`, `cli`, `tic-tac-toe`, `beginner`, `object-oriented-programming`

These coloured topic badges appear at the top of your repo and make it look polished. They also make your repo discoverable.

---

## Step 7 — Commit Strategy While Building the Project

This is where most beginners go wrong — they build the whole thing then do one commit saying "finished project". Instead, commit at every logical milestone as you build. For a TicTacToe project that history should look something like this:
```
feat: initialise project structure and entry point
feat: add board display function
feat: add player input and position validation
feat: implement win detection for rows and columns
feat: add diagonal win detection
feat: add draw detection
feat: add game loop and play again prompt
refactor: convert game logic into TicTacToe class
docs: add README with features and instructions
docs: add demo GIF to README
chore: add .gitignore and MIT licence
```

That commit history tells a story. Anyone reading it can follow exactly how you built the project step by step. It demonstrates genuine process, not just a finished result dropped online.

---

## Step 8 — Pin It to Your Profile

Once the repo is live and looking good, go to your GitHub profile page → click **Customize your pins** → select `tictactoe-python`. It will now appear as one of the featured repos on your profile homepage for anyone who visits.

---

## The Final Checklist Before Considering a Repo "Done"

Run through this for every project before pinning it or sharing the link:
```
✅ Repository name is lowercase with hyphens
✅ One-line description filled in on GitHub
✅ README has a title, description, features, how to run, what I learned
✅ Demo GIF or screenshot in the README
✅ .gitignore is present (no venv/ or __pycache__ visible in the repo)
✅ LICENSE file present
✅ Topics/tags added in the About section
✅ At least 5–6 meaningful commits with descriptive messages
✅ No passwords, API keys or .env files committed
✅ Code is readable — has comments where logic isn't obvious
✅ Pinned to profile if it's one of your best 6 projects
