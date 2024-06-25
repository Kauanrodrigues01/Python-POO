import datetime
import os
import pickle
import sys

class Task:
    """
    A class representing a task with a title, description, due date, and completion status.

    Attributes:
    title (str): The title of the task.
    description (str): The description of the task.
    due_date (datetime.date): The due date of the task.
    completed (bool): The completion status of the task.
    """

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = 'Done' if self.completed else 'Pending'
        return f"{self.title} (Due: {self.due_date}) - {status}\n{self.description}"

class TaskManager:
    """
    A class to manage tasks, allowing operations such as adding, viewing, updating, deleting, and saving tasks.

    Attributes:
    file_name (str): The name of the file where tasks are saved.
    tasks (list): The list of tasks.
    """

    def __init__(self, file_name='tasks.pkl'):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Load tasks from a file using pickle.

        Returns:
        list: The list of tasks loaded from the file, or an empty list if the file does not exist.
        """
        if os.path.exists(self.file_name):
            with open(self.file_name, 'rb') as f:
                return pickle.load(f)
        return []

    def save_tasks(self):
        """
        Save the current list of tasks to a file using pickle.
        """
        with open(self.file_name, 'wb') as f:
            pickle.dump(self.tasks, f)

    def add_task(self):
        """
        Add a new task by prompting the user for task details and saving the task.
        """
        title = input("Title: ")
        description = input("Description: ")
        due_date = input("Due Date (YYYY-MM-DD): ")
        try:
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Task not added.")
            return
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully.")

    def view_tasks(self):
        """
        Display all tasks with their details.
        """
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def update_task(self):
        """
        Update an existing task by prompting the user for task number and new details.
        """
        if not self.tasks:
            print("No tasks available to update.")
            return
        self.view_tasks()
        try:
            task_number = int(input("Enter task number to update: "))
            if task_number < 1 or task_number > len(self.tasks):
                print("Invalid task number.")
                return
        except ValueError:
            print("Invalid input.")
            return
        task = self.tasks[task_number - 1]
        print(f"Updating task: {task}")
        task.title = input(f"New title (leave blank to keep '{task.title}'): ") or task.title
        task.description = input(f"New description (leave blank to keep current): ") or task.description
        due_date = input(f"New due date (YYYY-MM-DD, leave blank to keep '{task.due_date}'): ")
        if due_date:
            try:
                task.due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Date not changed.")
        self.save_tasks()
        print("Task updated successfully.")

    def delete_task(self):
        """
        Delete an existing task by prompting the user for the task number.
        """
        if not self.tasks:
            print("No tasks available to delete.")
            return
        self.view_tasks()
        try:
            task_number = int(input("Enter task number to delete: "))
            if task_number < 1 or task_number > len(self.tasks):
                print("Invalid task number.")
                return
        except ValueError:
            print("Invalid input.")
            return
        task = self.tasks.pop(task_number - 1)
        self.save_tasks()
        print(f"Task '{task.title}' deleted successfully.")

    def mark_task_completed(self):
        """
        Mark an existing task as completed by prompting the user for the task number.
        """
        if not self.tasks:
            print("No tasks available to mark as completed.")
            return
        self.view_tasks()
        try:
            task_number = int(input("Enter task number to mark as completed: "))
            if task_number < 1 or task_number > len(self.tasks):
                print("Invalid task number.")
                return
        except ValueError:
            print("Invalid input.")
            return
        self.tasks[task_number - 1].completed = True
        self.save_tasks()
        print("Task marked as completed.")

    def clear_completed_tasks(self):
        """
        Clear all tasks that have been marked as completed after user confirmation.
        """
        completed_tasks = [task for task in self.tasks if task.completed]
        if not completed_tasks:
            print("No completed tasks to clear.")
            return
        print("Completed Tasks:")
        self.view_tasks()
        confirmation = input("Are you sure you want to clear all completed tasks? (yes/no): ").strip().lower()
        if confirmation == 'yes':
            self.tasks[:] = [task for task in self.tasks if not task.completed]
            self.save_tasks()
            print("Completed tasks cleared successfully.")
        else:
            print("Operation canceled.")

    def search_tasks(self):
        """
        Search for tasks by keyword in title or description.
        """
        keyword = input("Enter keyword to search for in tasks: ").lower()
        found_tasks = [task for task in self.tasks if keyword in task.title.lower() or keyword in task.description.lower()]
        if not found_tasks:
            print("No tasks found matching the keyword.")
        else:
            print(f"Found {len(found_tasks)} task(s) matching the keyword:")
            for task in found_tasks:
                print(task)

    def show_task_stats(self):
        """
        Display statistics about total tasks, completed tasks, and pending tasks.
        """
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        pending_tasks = total_tasks - completed_tasks
        print(f"Total Tasks: {total_tasks}")
        print(f"Completed Tasks: {completed_tasks}")
        print(f"Pending Tasks: {pending_tasks}")

    def save_and_exit(self):
        """
        Save all tasks and exit the program.
        """
        self.save_tasks()
        print("Tasks saved successfully.")
        sys.exit()

    def display_menu(self):
        """
        Display the main menu of options for the task manager.
        """
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Clear Completed Tasks")
        print("7. Search Tasks")
        print("8. Show Task Statistics")
        print("9. Save and Exit")

    def run(self):
        """
        Run the task manager, displaying the menu and handling user input.
        """
        while True:
            self.display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.mark_task_completed()
            elif choice == '6':
                self.clear_completed_tasks()
            elif choice == '7':
                self.search_tasks()
            elif choice == '8':
                self.show_task_stats()
            elif choice == '9':
                self.save_and_exit()
            else:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()