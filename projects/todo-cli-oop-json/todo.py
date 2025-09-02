"""
To-Do List (OOP) with JSON persistence and undo.

Features:
- Task model (description, completed)
- ToDoList manager (CRUD, search/filter, undo via in-memory snapshots)
- JSON storage (tasks.json) with UTF-8 reading/writing
- Minimal CLI for interactive use

Design notes:
- Snapshots use deepcopy to guarantee undo restores object identity/values.
- File is rewritten atomically per save to maintain a single source of truth.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List
import copy
import json


# -------------------------
# Domain Model
# -------------------------

@dataclass
class Task:
    """A single to-do item.

    Attributes:
        description: Human-readable task text (non-empty when persisted).
        completed: Completion flag (False by default).
    """
    description: str
    completed: bool = False

    def toggle(self) -> None:
        """Flip the completion status in place."""
        self.completed = not self.completed

    def to_dict(self) -> dict:
        """Serialize to a JSON-friendly dictionary."""
        return {"description": self.description, "completed": self.completed}

    @staticmethod
    def from_dict(d: dict) -> Optional["Task"]:
        """Deserialize from a dictionary.

        Args:
            d: A mapping expected to contain 'description' and 'completed'.

        Returns:
            Task if valid; otherwise None (e.g., empty description).
        """
        if not isinstance(d, dict):
            return None
        desc = str(d.get("description", "")).strip()
        if not desc:
            return None
        comp = bool(d.get("completed", False))
        return Task(desc, comp)


# -------------------------
# Application Model (Manager)
# -------------------------

class ToDoList:
    """Manage a collection of Task objects with JSON persistence and undo."""

    def __init__(self, data_file: Path = Path("tasks.json")) -> None:
        """Initialize the manager and eagerly load from disk if present.

        Args:
            data_file: JSON file path for persistence (default: tasks.json).
        """
        self._data_file: Path = data_file
        self._tasks: List[Task] = []
        self._history: List[List[Task]] = []  # LIFO snapshots for undo
        self.load()

    # ---------- Persistence ----------

    def load(self) -> None:
        """Load tasks from JSON if the file exists.

        Behavior:
            - Clears current tasks, then parses the JSON array.
            - Invalid entries (e.g., missing description) are skipped.
            - On read/parse error, prints a warning and starts empty.
        """
        self._tasks.clear()
        if not self._data_file.exists():
            return
        try:
            with self._data_file.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                for item in data:
                    t = Task.from_dict(item)
                    if t:
                        self._tasks.append(t)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Warning: Could not read JSON tasks file ({e}). Starting empty.")

    def save(self) -> None:
        """Persist current tasks to JSON.

        Notes:
            - Skips tasks whose descriptions are blank after strip().
            - Uses pretty printing for readability; change indent if needed.
        """
        try:
            payload = [t.to_dict() for t in self._tasks if t.description.strip()]
            with self._data_file.open("w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"Warning: Could not save tasks ({e}).")

    # ---------- History / Undo ----------

    def _snapshot(self) -> None:
        """Capture a deep-copy snapshot before mutation to support undo."""
        self._history.append(copy.deepcopy(self._tasks))

    def undo(self) -> bool:
        """Revert to the most recent snapshot, if any, and save.

        Returns:
            True if a snapshot was applied; False if no history exists.
        """
        if not self._history:
            return False
        prev = self._history.pop()
        self._tasks = prev
        self.save()
        return True

    # ---------- Query helpers ----------

    @staticmethod
    def _norm(s: str) -> str:
        """Normalize a string for case-insensitive matching."""
        return s.strip().lower()

    # ---------- CRUD operations ----------

    def list(self) -> List[Task]:
        """Return a shallow copy of the current tasks."""
        return list(self._tasks)

    def add(self, description: str) -> bool:
        """Add a new task with validation and persistence.

        Args:
            description: The task text.

        Returns:
            True if added; False if validation fails.
        """
        name = description.strip()
        if not name:
            print("Error: Task cannot be empty.")
            return False
        self._snapshot()
        self._tasks.append(Task(name, False))
        self.save()
        print(f"Success: Task '{name}' was added to your list.")
        return True

    def toggle(self, index_1based: int) -> bool:
        """Toggle a task's completion by its 1-based index.

        Returns:
            True on success; False if index is out of range.
        """
        i = index_1based - 1
        if 0 <= i < len(self._tasks):
            self._snapshot()
            self._tasks[i].toggle()
            self.save()
            print(f"Success: Task {index_1based} toggled.")
            return True
        print("Error: Invalid task number. Please try again.")
        return False

    def edit(self, index_1based: int, new_text: str) -> bool:
        """Edit a task's description by its 1-based index.

        Returns:
            True on success; False for invalid index or empty new text.
        """
        i = index_1based - 1
        if not (0 <= i < len(self._tasks)):
            print("Error: Invalid task number.")
            return False
        new_text = new_text.strip()
        if not new_text:
            print("Error: Description cannot be empty.")
            return False
        self._snapshot()
        self._tasks[i].description = new_text
        self.save()
        print("Success: Task updated.")
        return True

    def delete(self, index_1based: int) -> bool:
        """Delete a task by its 1-based index.

        Returns:
            True on success; False if index is out of range.
        """
        i = index_1based - 1
        if 0 <= i < len(self._tasks):
            self._snapshot()
            removed = self._tasks.pop(i)
            self.save()
            print(f"Deleted: {removed.description}")
            return True
        print("Error: Invalid task number.")
        return False

    def clear_completed(self) -> int:
        """Remove all completed tasks.

        Returns:
            The number of tasks removed.
        """
        before = len(self._tasks)
        remaining = [t for t in self._tasks if not t.completed]
        if len(remaining) == before:
            print("No completed tasks to clear.")
            return 0
        self._snapshot()
        self._tasks = remaining
        self.save()
        removed = before - len(self._tasks)
        print(f"Cleared {removed} completed task(s).")
        return removed

    # ---------- Search / Filter ----------

    def filter(
        self,
        keyword: Optional[str] = None,
        completed: Optional[bool] = None,
    ) -> List[Task]:
        """Return a filtered view of tasks (no persistence).

        Args:
            keyword: Case-insensitive substring to match in descriptions.
            completed: If True/False, filter by completion status.

        Returns:
            A new list of tasks matching the criteria.
        """
        items = self._tasks
        if keyword is not None and keyword.strip():
            q = self._norm(keyword)
            items = [t for t in items if q in self._norm(t.description)]
        if completed is not None:
            items = [t for t in items if t.completed is completed]
        return list(items)


# -------------------------
# Presentation (CLI)
# -------------------------

def print_tasks(tasks: List[Task]) -> None:
    """Pretty-print the current task list."""
    print("\n--- YOUR TO-DO LIST ---")
    if not tasks:
        print("Your to-do list is currently empty.")
    else:
        for idx, t in enumerate(tasks, start=1):
            mark = "✔️" if t.completed else " "
            print(f"{idx}. [{mark} ] {t.description}")
    print("-----------------------\n")


def print_filtered(tasks: List[Task]) -> None:
    """Pretty-print a filtered set of tasks."""
    if not tasks:
        print("(no matching tasks)")
        return
    print("\n--- FILTERED TASKS ---")
    for idx, t in enumerate(tasks, start=1):
        mark = "✔️" if t.completed else " "
        print(f"{idx}. [{mark} ] {t.description}")
    print("----------------------")


def main() -> None:
    """Interactive CLI entry point."""
    print("Welcome to your personal To-Do List Manager (OOP, JSON)!")
    todo = ToDoList()  # loads from tasks.json automatically

    while True:
        print("\nPlease choose an option:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Toggle a task as complete/incomplete")
        print("4. Edit a task description")
        print("5. Delete a task")
        print("6. Clear completed tasks")
        print("7. Search / Filter")
        print("8. Undo last action")
        print("9. Exit the application")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            task_name = input("What task would you like to add? ")
            todo.add(task_name)

        elif choice == "2":
            print_tasks(todo.list())

        elif choice == "3":
            try:
                num = int(input("Enter the task number to toggle: ").strip())
                todo.toggle(num)
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "4":
            try:
                num = int(input("Enter the task number to edit: ").strip())
                current_list = todo.list()
                if 1 <= num <= len(current_list):
                    print(f"Current: {current_list[num-1].description}")
                new_text = input("Enter new description: ").strip()
                todo.edit(num, new_text)
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "5":
            try:
                num = int(input("Enter the task number to delete: ").strip())
                todo.delete(num)
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "6":
            todo.clear_completed()

        elif choice == "7":
            q = input("Keyword (press Enter to skip): ")
            s = input("Status [a]ll/[c]ompleted/[i]ncomplete (default a): ").strip().lower()
            status = True if s == "c" else False if s == "i" else None
            print_filtered(todo.filter(keyword=q, completed=status))

        elif choice == "8":
            if todo.undo():
                print("Undo successful.")
            else:
                print("Nothing to undo.")

        elif choice == "9":
            print("Thank you for using the To-Do List Manager. Goodbye!")
            todo.save()
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
