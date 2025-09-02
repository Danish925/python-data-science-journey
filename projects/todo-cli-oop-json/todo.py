"""
To-Do List Application in Python

This script implements a command-line to-do list manager with the following features:
- Add, view, edit, toggle (complete/incomplete), delete, and clear completed tasks.
- Save tasks persistently to a text file and load on startup.
- Undo capability with snapshot history to revert the last change.
- Search and filter tasks by keywords and completion status.

Author: [Your Name]
Date: August 2025
"""

from pathlib import Path
from typing import Optional
import copy

# Global variables
tasks: list[dict] = []              # Main list to hold task dictionaries
history: list[list[dict]] = []      # Stack to hold snapshots of task states for undo support
DATA_FILE: Path = Path("tasks.txt") # Path to the file for task persistence


# -------------------------
# Persistence Functions
# -------------------------
def load_tasks() -> None:
    """
    Load tasks from the persistent file into the tasks list.
    Each line in the file should be prefixed by [ ] or [x] indicating completion status.
    """
    tasks.clear()
    if not DATA_FILE.exists():
        return
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                if line.startswith("[ ] "):
                    desc = line[4:].strip()
                    if desc:
                        tasks.append({"description": desc, "completed": False})
                elif line.startswith("[x] "):
                    desc = line[4:].strip()
                    if desc:
                        tasks.append({"description": desc, "completed": True})
                else:
                    desc = line.strip()
                    if desc:
                        tasks.append({"description": desc, "completed": False})
    except OSError as e:
        print(f"Warning: Could not read tasks file ({e}). Starting empty.")


def save_tasks() -> None:
    """
    Save all tasks to the persistent file.
    Each task is saved with a prefix indicating completion status.
    """
    try:
        with DATA_FILE.open("w", encoding="utf-8") as f:
            for t in tasks:
                status = "[x]" if t.get("completed") else "[ ]"
                desc = str(t.get("description", "")).strip()
                if desc:
                    f.write(f"{status} {desc}\n")
    except OSError as e:
        print(f"Warning: Could not save tasks ({e}).")


# -------------------------
# Undo Support Functions
# -------------------------
def snapshot() -> None:
    """
    Take a deep copy snapshot of the current tasks list
    and push it onto the history stack to enable undo.
    """
    history.append(copy.deepcopy(tasks))


def undo() -> bool:
    """
    Restore tasks to the last saved snapshot, if any.
    Returns True if undo was performed, False if no undo possible.
    """
    if not history:
        return False
    prev = history.pop()
    tasks.clear()
    tasks.extend(prev)
    save_tasks()
    return True


# -------------------------
# Helper Functions for Searching and Filtering
# -------------------------
def normalize(s: str) -> str:
    """Normalize strings for case-insensitive comparison."""
    return s.strip().lower()


def safe_desc(t: dict) -> str:
    """Safely get a task's description."""
    return str(t.get("description", "")).strip()


def filter_by_keyword(items: list[dict], query: str) -> list[dict]:
    """Filter tasks containing the query keyword (case-insensitive)."""
    q = normalize(query)
    if not q:
        return items[:]
    return [t for t in items if q in normalize(safe_desc(t))]


def filter_by_status(items: list[dict], completed: Optional[bool]) -> list[dict]:
    """Filter tasks by their completion status."""
    if completed is None:
        return items[:]
    return [t for t in items if bool(t.get("completed", False)) == completed]


def filter_tasks(items: list[dict], query: Optional[str] = None,
                 completed: Optional[bool] = None) -> list[dict]:
    """Filter tasks by keyword and/or completion status."""
    result = items
    if query is not None:
        result = filter_by_keyword(result, query)
    if completed is not None:
        result = filter_by_status(result, completed)
    return result


# -------------------------
# Core Task Management Functions
# -------------------------
def add_task(task_name: str) -> None:
    """Add a new task to the to-do list, after validating and snapshotting."""
    name = task_name.strip()
    if not name:
        print("Error: Task cannot be empty.")
        return
    snapshot()
    tasks.append({"description": name, "completed": False})
    save_tasks()
    print(f"Success: Task '{name}' was added to your list.")


def view_tasks() -> None:
    """Print all tasks with their status and numbering."""
    print("\n--- YOUR TO-DO LIST ---")
    if not tasks:
        print("Your to-do list is currently empty.")
    else:
        for index, task in enumerate(tasks, start=1):
            mark = "✔️" if task.get("completed") else " "
            print(f"{index}. [{mark} ] {task.get('description', '')}")
    print("-----------------------\n")


def mark_task_complete(task_number: int) -> None:
    """
    Toggle the completion status of a specified task by its number.
    """
    i = task_number - 1
    if 0 <= i < len(tasks):
        snapshot()
        tasks[i]["completed"] = not bool(tasks[i].get("completed", False))
        save_tasks()
        print(f"Success: Task {task_number} toggled.")
    else:
        print("Error: Invalid task number. Please try again.")


def edit_task(task_number: int) -> None:
    """
    Edit the description of a specified task by its number, with validation.
    """
    i = task_number - 1
    if not (0 <= i < len(tasks)):
        print("Error: Invalid task number.")
        return
    current = safe_desc(tasks[i])
    print(f"Current: {current}")
    new_text = input("Enter new description: ").strip()
    if not new_text:
        print("Error: Description cannot be empty.")
        return
    snapshot()
    tasks[i]["description"] = new_text
    save_tasks()
    print("Success: Task updated.")


def delete_task(task_number: int) -> None:
    """
    Remove the specified task from the list after snapshotting.
    """
    i = task_number - 1
    if 0 <= i < len(tasks):
        snapshot()
        removed = tasks.pop(i)
        save_tasks()
        print(f"Deleted: {removed.get('description', '')}")
    else:
        print("Error: Invalid task number.")


def clear_completed() -> None:
    """Remove all completed tasks from the list after snapshotting."""
    before = len(tasks)
    remaining = [t for t in tasks if not t.get("completed", False)]
    if len(remaining) == before:
        print("No completed tasks to clear.")
        return
    snapshot()
    tasks[:] = remaining
    save_tasks()
    print(f"Cleared {before - len(tasks)} completed task(s).")


# -------------------------
# Main Program Loop
# -------------------------
def main() -> None:
    """
    The main interactive loop that displays options to the user,
    takes input, and performs actions accordingly.
    """
    print("Welcome to your personal To-Do List Manager!")
    load_tasks()
    
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
        
        if choice == '1':
            task_name = input("What task would you like to add? ")
            add_task(task_name)
        
        elif choice == '2':
            view_tasks()
        
        elif choice == '3':
            try:
                num = int(input("Enter the task number to toggle: ").strip())
                mark_task_complete(num)
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == '4':
            try:
                num = int(input("Enter the task number to edit: ").strip())
                edit_task(num)
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == '5':
            try:
                num = int(input("Enter the task number to delete: ").strip())
                delete_task(num)
            except ValueError:
                print("Error: Please enter a valid number.")
        
        elif choice == '6':
            clear_completed()
        
        elif choice == '7':
            q = input("Keyword (press Enter to skip): ")
            s = input("Status [a]ll/[c]ompleted/[i]ncomplete (default a): ").strip().lower()
            status = True if s == "c" else False if s == "i" else None
            results = filter_tasks(tasks, query=q, completed=status)
            if not results:
                print("(no matching tasks)")
            else:
                print("\n--- FILTERED TASKS ---")
                for idx, t in enumerate(results, start=1):
                    mark = "✔️" if t.get("completed") else " "
                    print(f"{idx}. [{mark} ] {t.get('description', '')}")
                print("----------------------")
        
        elif choice == '8':
            if undo():
                print("Undo successful.")
            else:
                print("Nothing to undo.")
        
        elif choice == '9':
            print("Thank you for using the To-Do List Manager. Goodbye!")
            save_tasks()
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()
