# PYTHON-DATA-SCIENCE-JOURNEY

## Overview
A beginner-friendly, hands-on journey into Python for data science—mini-projects, scripts, and notebooks that build skills progressively. This repository tracks my learning path from Python fundamentals and OOP to a complete data analysis and visualization pipeline.

---

## 📂 Repository Structure

* **[data-visualization](./data-visualization/)**: Contains all scripts and notebooks for the data analysis and visualization pipeline, focusing on Pandas for data wrangling and Matplotlib/Seaborn for plotting.
* **[projects](./projects/)**: Self-contained, multi-file projects focusing on Object-Oriented Programming (OOP) concepts. Each has its own README.
* **[scripts](./scripts/)**: A collection of 10+ single-file, runnable mini-projects and utilities (games, tools, etc.). See the [scripts README](./scripts/README.md) for a full list.
* **[notebooks](./notebooks/)**: Jupyter Notebooks used for experimentation, incremental learning, and scratch work.

---

## 💡 Highlights

* **10+ mini Python projects** focusing on clean code, input validation, and interactive CLIs.
* Practice across **control flow, loops, randomness, error handling, and file I/O**.
* Progression from Python basics to **persistence (JSON), Object-Oriented Programming (OOP), and data visualization** (pandas/NumPy/Matplotlib).
* **Organized projects** with per-project `README.md` files and runnable entry points.

---

## 🏆 Featured Projects

### 1. [Secure Password Generator (OOP, secrets)](./projects/password-generator-oop/)
* **Folder:** `[projects/password-generator-oop](./projects/password-generator-oop/)`
* **Entry:** `[main.py](./projects/password-generator-oop/main.py)`
* **Summary:** Policy-driven generator using the OS-backed `secrets` module; guarantees at least one character from each enabled class.

### 2. [To-Do CLI (OOP + JSON + undo)](./projects/todo-cli-oop-json/)
* **Folder:** `[projects/todo-cli-oop-json](./projects/todo-cli-oop-json/)`
* **Entry:** `[todo.py](./projects/todo-cli-oop-json/todo.py)`
* **Summary:** OOP task manager with JSON persistence, case-insensitive search/filter, and snapshot-based undo via `deepcopy`.

### 3. [Zoo Simulator (OOP: inheritance + polymorphism)](./projects/zoo-sim-oop/)
* **Folder:** `[projects/zoo-sim-oop](./projects/zoo-sim-oop/)`
* **Entry:** `[zoo.py](./projects/zoo-sim-oop/zoo.py)`
* **Summary:** CLI zoo manager with Animal → Mammal/Bird/Reptile inheritance, exhibits with capacity, a polymorphic “daily show,” and time-based hunger/feeding.

---

## 🗺️ Roadmap

### ✅ In Progress
* **Data Analysis Stack:** Building a complete data cleaning and visualization pipeline using Pandas, Matplotlib, and Seaborn. All work is being tracked in the `[data-visualization](./data-visualization/)` folder.

### 🔜 Future Goals
* Add JSON persistence and unit tests for selected scripts.
* Explore more advanced statistical analysis and visualization.
* Begin introduction to Machine Learning models and Scikit-learn.
* Grow the portfolio with more advanced EDA exercises.

---

## 🚀 Getting Started

1.  **Requirement:** Python 3.9+ recommended.
2.  **Clone:**
    ```sh
    git clone [https://github.com/Danish925/python-data-science-journey](https://github.com/Danish925/python-data-science-journey)
    cd python-data-science-journey
    ```
3.  **Run a Project:**
    ```sh
    # Password Generator
    cd projects/password-generator-oop
    python main.py
    
    # To-Do CLI
    cd projects/todo-cli-oop-json
    python todo.py
    
    # Zoo Simulator
    cd projects/zoo-sim-oop
    python zoo.py
    ```
4.  **Run a Script:**
    ```sh
    python scripts/quiz_game.py
    ```
5.  **Tip (Windows):** Use `py` instead of `python` if `python` is not recognized.

---

## ✨ Why These Projects

* **Security:** Passwords use OS-backed CSPRNG via `secrets`; non-crypto RNG is avoided.
* **Reliability:** To-Do state uses human-readable JSON via `json.load`/`json.dump` with `UTF-8` and `indent=2`.
* **Design:** Classes separate concerns (e.g., `Task`/`ToDoList`, `PasswordPolicy`/`PasswordGenerator`, `Animal`/`Zoo`), making features easier to extend and test.

---

## 🤝 Contributing

1.  Issues and suggestions are welcome—open a discussion or PR with a clear description.
2.  Use clear commit messages (e.g., `feat:`, `fix:`, `docs:`) for readable history.
3.  Prefer relative links in Markdown for navigation inside the repo.
