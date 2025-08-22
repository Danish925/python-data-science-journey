Title
python-data-science-journey

Overview
A beginner-friendly journey into Python for data science. This repository documents a hands‑on learning path with scripts, mini‑projects, and Jupyter Notebooks—covering Python basics, data handling, and visualization on the path to full data science proficiency.

Highlights

10+ mini Python projects focused on clean functions, input validation, and small CLIs.

Practice across control flow, loops, randomness, error handling, and file I/O.

Roadmap‑aligned learning: foundations → persistence and OOP → pandas, NumPy, and visualization.

New: To‑Do CLI with human‑readable TXT persistence ([ ]/[x] format).

Projects (selected)

Powerful Password Generator: Secure passwords with configurable length and character sets; robust input validation.

Simple Quiz Game: Asks questions, tracks score, and provides feedback—good practice in loops and state.

Dice Rolling Simulator: Randomness and replay loop with clean structure.

Number Guessing Game: While loops, conditional logic, and try/except for robust error handling.

Simple Countdown Timer: Input checks, time.sleep, and mm:ss formatting.

NEW — To‑Do CLI (TXT persistence):

Add, list, mark complete, delete, and clear completed.

Saves to tasks.txt in a readable format: “[ ] description” / “[x] description”.

Cross‑platform paths (pathlib), UTF‑8 safe.

How to run
Requirements: Python 3.10+.

Clone:

git clone https://github.com/Danish925/python-data-science-journey

cd python-data-science-journey

Run any script:

Password Generator: python password_generator.py

Quiz Game: python quiz_game.py

Dice Roller: python dice_roller.py

Countdown Timer: python countdown_timer.py

To‑Do CLI (TXT): python tasks.py

Tip (Windows): if python is not found, use py instead (e.g., py tasks.py).

To‑Do CLI details

File: tasks.py

Features:

Add tasks, view tasks, mark complete, delete tasks, clear completed

Human‑readable persistence to tasks.txt (UTF‑8)

File format:

 Buy milk

 Read 10 pages

Notes:

Blank lines are ignored on load.

Unknown prefixes are treated as incomplete for robustness.

Learning roadmap (next steps)

File I/O and persistence: DONE (To‑Do app saves/loads data cleanly).

OOP refactor: Task/ToDoList classes, JSON persistence, tests.

Analytics toolkit: pandas, NumPy, Matplotlib/Seaborn with EDA notebooks.

Repo info

Pinned on my GitHub profile for easy access.

Releases will be tagged per milestone (e.g., v0.2.0 “Persistence”, v0.3.0 “OOP Refactor”).

Optional “Coming soon” (if you plan to add soon)

Search/filter by keyword and completion status.

Toggle complete (on/off).

Edit task descriptions.

Undo last action (single‑step history).
