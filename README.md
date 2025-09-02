python-data-science-journey

Overview

A beginner-friendly, hands-on journey into Python for data science—mini-projects, scripts, and notebooks that build a strong foundation step by step. The repository now highlights two structured OOP projects alongside practice scripts and learning notebooks.

Highlights

1.10+ mini Python projects focusing on clean code, input validation, and interactive CLIs.

2.Practice across control flow, loops, randomness, error handling, and file I/O.

3.Progression from basics to persistence, OOP, and visualization with pandas/NumPy/Matplotlib/Seaborn.

4.Newly organized projects/ with per‑project READMEs and runnable entry points.

Projects

1.Secure Password Generator (OOP, secrets)

Folder: projects/password-generator-oop

Entry: projects/password-generator-oop/main.py

Summary: Policy‑driven generator using the OS‑backed secrets module; guarantees at least one character from each enabled class; prints 3 passwords.

Open: Folder - main.py

2.To‑Do CLI (OOP + JSON + undo)

Folder: projects/todo-cli-oop-json

Entry: projects/todo-cli-oop-json/todo.py

Summary: OOP task manager with JSON persistence, case‑insensitive search/filter, and snapshot‑based undo via deepcopy.

Open: Folder - todo.py

Selected mini-projects

1.Powerful Password Generator (earlier procedural version) – configurable secure passwords with robust input checks.

2.Simple Quiz Game – interactive Q&A with score tracking.

3.Dice Rolling Simulator – randomness exploration with replay loop.

4.Number Guessing Game – loops plus try/except input handling.

5.Simple Countdown Timer – input validation and time display formatting.

Repository layout

1.projects/ — self‑contained mini‑apps with their own README and entry script.

2.scripts/ — small single‑file exercises such as dice_roller.py, quiz_game.py, countdown_timer.py.

3.notebooks/ — Jupyter notebooks for incremental learning and experimentation.

4.data/ — optional raw/ and processed/ subfolders (with a data README when used).

Getting started

1.Requirement: Python 3.9+ recommended.

2.Clone:

git clone https://github.com/Danish925/python-data-science-journey

cd python-data-science-journey

3.Run a project:

Password Generator: cd projects/password-generator-oop && python main.py

To‑Do CLI: cd projects/todo-cli-oop-json && python todo.py

Scripts: python scripts/quiz_game.py (etc.)

4.Tip (Windows): use py instead of python if python is not recognized.

Why these projects

1.Security: Passwords are generated with secrets.SystemRandom for cryptographic randomness; random is intentionally avoided.

2.Reliability: To‑Do state is stored as human‑readable JSON via json.load/json.dump with UTF‑8 and indent=2.

3.Design: Classes separate concerns (Task/ToDoList, PasswordPolicy/PasswordGenerator), making features easier to extend and test.

Roadmap

1.JSON persistence and unit tests for selected scripts and projects.

2.Data analytics stack: pandas, NumPy, visualization (Matplotlib/Seaborn) notebooks.

3.Additional mini‑projects and EDA exercises to grow the portfolio.

Contributing

1.Issues and suggestions are welcome—open a discussion or PR with a clear description.

2.Use clear commit messages (e.g., feat:, fix:, docs:) for readable history.

3.Prefer relative links in Markdown for navigation inside the repo.
