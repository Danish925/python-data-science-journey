# --- Persistent To-Do List Application ---
# A command-line To-Do list that saves tasks to a file to be persistent
# between sessions.

def load_tasks(filename="tasks.txt"):
    """
    Loads tasks from a text file. Handles FileNotFoundError if the file doesn't exist.
    
    Returns:
        list: A list of tasks from the file, or an empty list if file not found.
    """
    try:
        with open(filename, 'r') as file:
            # .strip() removes the newline characters from each line read.
            tasks = [line.strip() for line in file.readlines()]
            return tasks
    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty list.
        return []

def save_tasks(tasks_list, filename="tasks.txt"):
    """
    Saves the complete list of tasks to a text file, overwriting its contents.
    
    Args:
        tasks_list (list): The current list of tasks to save.
    """
    with open(filename, 'w') as file:
        for task in tasks_list:
            file.write(f"{task}\n")

def show_tasks(tasks_list):
    """Displays all tasks in a numbered, user-friendly format."""
    print("\n--- Your To-Do List ---")
    if not tasks_list:
        print("Your list is currently empty.")
    else:
        for i, task in enumerate(tasks_list, 1):
            print(f"{i}. {task}")
    print("-----------------------")

def add_task(tasks_list):
    """Adds a new task to the list and saves the updated list to the file."""
    task = input("Enter the new task: ")
    tasks_list.append(task)
    # Immediately save the list to ensure the new task is persistent.
    save_tasks(tasks_list)
    print(f"Task '{task}' has been added.")

def main():
    """Main function to run the To-Do List application's event loop."""
    
    # Load any existing tasks from the file right at the start.
    tasks = load_tasks()
    
    print("--- Welcome to your Persistent To-Do List! ---")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Show tasks")
        print("2. Add a task")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Ensures that main() is called only when the script is executed directly.
if __name__ == "__main__":
    main()
