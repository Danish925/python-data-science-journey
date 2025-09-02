Title
To‑Do CLI (OOP + JSON + undo)

Overview

1.A terminal To‑Do application using an object‑oriented design with Task and ToDoList classes for clear separation of concerns.

2.Persists tasks in a human‑readable tasks.json file using Python’s json module with UTF‑8 and pretty printing.

3.Supports add/edit/toggle/delete, clear completed, case‑insensitive search/filter, and single‑step undo via snapshot history.

Why this project

1.Demonstrates stateful CLI software with reliable file I/O and a clean domain model rather than ad‑hoc scripts.

2.Uses JSON instead of custom text parsing for safer schema evolution and simpler persistence.

Features

1.OOP structure: Task holds description/completed, ToDoList manages collection, persistence, and history.

2.JSON persistence: tasks.json written with json.dump(..., ensure_ascii=False, indent=2) and read with json.load.

3.Undo: Deep‑copy snapshots before each mutation allow a single step of revert to the previous state.

4.Search/filter: Keyword matching is case‑insensitive; optional filter by completed True/False.

Requirements

1.Python 3.9+; no third‑party dependencies are required for the CLI and storage.

Project files

1.todo.py: Main entry point containing Task/ToDoList, CLI menu, and JSON persistence.

2.tasks.json (created on first save): Array of task objects on disk.

JSON format

1.The file stores a single array; each element is an object with description and completed fields.

Example:
[
{"description": "Practice Python", "completed": false},
{"description": "Read docs", "completed": true}
]

Run

1.python todo.py to start the interactive menu in the terminal.

2.The app automatically loads from tasks.json if present and saves after mutations.

Common commands (via menu)

1.Add a task: enter description and confirm to persist to tasks.json.

2.Toggle completion: provide the 1‑based index to flip completed/incomplete.

3.Edit description: update the text for a given index; blank descriptions are rejected.

4.Delete a task: remove by index and save the updated list to disk.

5.Clear completed: remove all tasks marked complete and report how many were cleared.

6.Search/filter: provide a keyword and choose status all/completed/incomplete.

7.Undo: revert the last change (add/edit/toggle/delete/clear) using the previous snapshot.

Design notes

1.Persistence: UTF‑8 text with ensure_ascii=False preserves non‑ASCII characters; indent=2 keeps files readable and easy to diff.

2.Robustness: On malformed JSON or read error, loading warns and starts empty to avoid crashes.

3.Extensibility: JSON schema can be extended later (e.g., priority or due_date); Task.to_dict/from_dict isolates this logic.

Example (library usage)

from todo import ToDoList
todo = ToDoList()
todo.add("Practice Python")
todo.toggle(1); todo.undo()
print([t.to_dict() for t in todo.filter(keyword="python")])

Troubleshooting

1.“Nothing to undo”: The history is empty; perform a change first (e.g., add, edit, toggle) to create a snapshot.

2.“Warning: Could not read JSON tasks file”: tasks.json may be malformed; the app will start with an empty list and overwrite on next save. Back up the file if manual recovery is needed.
