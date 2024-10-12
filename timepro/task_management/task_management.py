import json
import csv
from enum import Enum
from datetime import datetime, timedelta

class TaskPriority(Enum):
    """
    Enum for task priority levels.

    Atributes:
        LOW (int): The task has low priority.
        MEDIUM (int): The task has medium priority.
        HIGH (int): The task has high priority.
    """
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class TaskStatus(Enum):
    """
    Enum for task status.

    Atributes:
        WAITING (int): The task is waiting.
        IN_PROGRESS (int): The task is in progress.
        COMPLETED (int): The task is completed.
    """
    WAITING = 0
    IN_PROGRESS = 1
    COMPLETED = 2

class Task:
    """
    A class to represent a task.

    Attributes:
        title (str): The title of the task.
        description (str): A brief description of the task.
        priority (TaskPriority): The priority level of the task.
        deadline_date (datetime): The deadline for the task.
        status (TaskStatus): The current status of the task.
        created_date (datetime): The date when the task was created.
        tags (set): A set of tags associated with the task.

    """

    def __init__(self, title, description="", priority=TaskPriority.MEDIUM, deadline_date=None, status=TaskStatus.WAITING, created_date=datetime.now(), tags=set()):
        """
        Initializes a Task instance.

        Args:
            title (str): The title of the task.
            description (str): A brief description of the task.
            priority (TaskPriority): The priority level of the task (default is TaskPriority.MEDIUM).
            deadline_date (str or datetime): The deadline for the task in 'YYYY-MM-DD HH:MM' format or datetime object (default is now).
            status (TaskStatus): The current status of the task (default is TaskStatus.WAITING).
            created_date (datetime): The date when the task was created (default is now).
            tags (set): A set of tags associated with the task (default is an empty set).
        """
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline_date = self._parse_deadline(deadline_date)
        self.status = TaskStatus.WAITING
        self.created_date = datetime.now()
        self.tags = set()
        print(f"Task created: {self.title}")

    def _parse_deadline(self, deadline_date):
        """
        Parses the deadline date.

        Args:
            deadline_date (str or datetime): The deadline for the task.

        Returns:
            datetime: The parsed deadline date.

        Raises:
            ValueError: If the date format is invalid.
        """
        if isinstance(deadline_date, str):
            try:
                return datetime.strptime(deadline_date, "%Y-%m-%d %H:%M")
            except ValueError:
                try:
                    return datetime.strptime(deadline_date, "%Y-%m-%d")
                except ValueError:
                    raise ValueError("Invalid date format. Use 'YYYY-MM-DD' or 'YYYY-MM-DD HH:MM'.")
        elif isinstance(deadline_date, datetime):
            return deadline_date
        return datetime.now()

    def mark_completed(self):
        """
        Marks the task as completed.
        """
        self.status = TaskStatus.COMPLETED
        print(f"Task marked as completed: {self.title}")

    def update_status(self, status):
        """
        Updates the status of the task.

        Args:
            status (TaskStatus): The new status to set.

        Raises:
            ValueError: If the provided status is not a TaskStatus enum.
        """
        if isinstance(status, TaskStatus):
            self.status = status
            print(f"Status updated for task '{self.title}': {status.name}")
        else:
            print(f"Invalid status for task '{self.title}'. Use TaskStatus enum.")

    def add_tag(self, tag):
        """
        Adds a tag to the task.

        Args:
            tag (str): The tag to add.
        """
        self.tags.add(tag.lower())
        print(f"Tag added to task '{self.title}': {tag}")

    def remove_tag(self, tag):
        """
        Removes a tag from the task.

        Args:
            tag (str): The tag to remove.
        """
        self.tags.discard(tag.lower())
        print(f"Tag removed from task '{self.title}': {tag}")

    def is_overdue(self):
        """
        Checks if the task is overdue.

        Returns:
            bool: True if the task is overdue, False otherwise.
        """
        is_overdue = datetime.now() > self.deadline_date and self.status != TaskStatus.COMPLETED
        print(f"Task '{self.title}' overdue status: {is_overdue}")
        return is_overdue
    
    def time_remaining(self):
        """
        Calculates the time remaining until the deadline.

        Returns:
            timedelta: The time remaining until the deadline, or None if no deadline is set.
        """
        if self.deadline_date:
            remaining = self.deadline_date - datetime.now()
            print(f"Time remaining for task '{self.title}': {remaining}")
            return remaining
        print(f"No deadline set for task '{self.title}'")
        return None

    def __str__(self):
        """
        Returns a string representation of the task.
        """
        return f"{self.title} - Status : {self.status.name}, Deadline: {self.deadline_date}, Priority: {self.priority.name}"


class TaskManager:
    """
    A class to manage tasks.

    Attributes:
        tasks (list): A list to store Task objects.
    """

    def __init__(self):
        """
        Initializes the TaskManager instance with an empty task list.
        """
        self.tasks = []
        print("TaskManager initialized")

    def add_task(self, task):
        """
        Adds a task to the manager.

        Args:
            task (Task): The task to add.

        Raises:
            TypeError: If the provided object is not a Task.
        """
        if isinstance(task, Task):
            self.tasks.append(task)
            print(f"Task added: {task.title}")
        else:
            print("Error: Only Task objects can be added.")

    def remove_task(self, title):
        """
        Removes a task by title.

        Args:
            title (str): The title of the task to remove.
        """
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.title != title]
        removed_count = initial_count - len(self.tasks)
        print(f"Removed {removed_count} task(s) with title: {title}")

    def get_task(self, title):
        """
        Gets a task by title.

        Args:
            title (str): The title of the task to retrieve.

        Returns:
            Task: The task object if found, None otherwise.
        """
        task = next((task for task in self.tasks if task.title == title), None)
        print(f"Retrieved task: {task.title if task else 'None'}")
        return task

    def list_tasks(self, filter_by_status=None):
        """
        Lists all tasks or filters by status.

        Args:
            filter_by_status (TaskStatus): The status to filter by (optional).

        Returns:
            list: A list of tasks.
        """
        if filter_by_status:
            filtered_tasks = [task for task in self.tasks if task.status == filter_by_status]
            print(f"Listed {len(filtered_tasks)} tasks with status: {filter_by_status.name}")
            return filtered_tasks
        print(f"Listed all {len(self.tasks)} tasks")
        return self.tasks
    
    def upcoming_tasks(self, days=7):
        """Gets upcoming tasks within a specified number of days.

        Args:
            days (int): The number of days to look ahead (default is 7).

        Returns:
            list: A list of upcoming tasks.
        """
        future_date = datetime.now() + timedelta(days=days)
        upcoming = [task for task in self.tasks if task.deadline_date <= future_date and task.status != TaskStatus.COMPLETED]
        print(f"Found {len(upcoming)} upcoming tasks in the next {days} days")
        return upcoming


    def tasks_by_priority(self, priority):
        """Gets tasks filtered by priority.

        Args:
            priority (TaskPriority): The priority to filter by.

        Returns:
            list: A list of tasks with the specified priority.
        """
        priority_tasks = [task for task in self.tasks if task.priority == priority]
        print(f"Found {len(priority_tasks)} tasks with priority: {priority.name}")
        return priority_tasks

    def pending_tasks(self):
        """
        Gets all pending tasks.

        Returns:
            list: A list of tasks that are not completed.
        """
        pending = [task for task in self.tasks if task.status != TaskStatus.COMPLETED]
        print(f"Found {len(pending)} pending tasks")
        return pending
    
    def get_overdue_tasks(self):
        """Gets all overdue tasks.

        Returns:
            list: A list of overdue tasks.
        """
        overdue = [task for task in self.tasks if task.is_overdue()]
        print(f"Found {len(overdue)} overdue tasks")
        return overdue


    def get_tasks_by_tag(self, tag):
        """Gets tasks filtered by a specific tag.

        Args:
            tag (str): The tag to filter by.

        Returns:
            list: A list of tasks with the specified tag.
        """
        tagged_tasks = [task for task in self.tasks if tag.lower() in task.tags]
        print(f"Found {len(tagged_tasks)} tasks with tag: {tag}")
        return tagged_tasks


    def generate_task_report(self):
        """Generates a report of the tasks.

        Returns:
            str: A formatted string report of the task manager's status.
        """
        report = "Task Manager Report\n"
        report += "====================\n\n"
        
        report += f"Total Tasks: {len(self.tasks)}\n"
        report += f"Completed Tasks: {len(self.list_tasks(TaskStatus.COMPLETED))}\n"
        report += f"Pending Tasks: {len(self.pending_tasks())}\n"
        report += f"Overdue Tasks: {len(self.get_overdue_tasks())}\n\n"
        
        report += "Tasks by Priority:\n"
        for priority in TaskPriority:
            count = len(self.tasks_by_priority(priority))
            report += f"  {priority.name}: {count}\n"
        
        report += "\nUpcoming Tasks (Next 7 Days):\n"
        for task in self.upcoming_tasks():
            report += f"  {task}\n"
        
        report += "\nDetailed Task List:\n"
        for task in self.tasks:
            report += f"\n{task}\n"
            report += f"  Description: {task.description}\n"
            report += f"  Created Date: {task.created_date}\n"
            report += f"  Tags: {', '.join(task.tags) if task.tags else 'None'}\n"
        
        return report

class TaskFileManager:
    def __init__(self):
        self.tasks = []

    def save_tasks_to_json(self, file_path):
        """
        Saves the tasks to a JSON file.

        Args:
            file_path (str): The path to the file where tasks should be saved.

        Raises:
            IOError: If there's an error reading from the file.
            ValueError: If the JSON data is invalid.
        """
        print(f"Saving tasks to JSON file: {file_path}")
        tasks_data = []
        for task in self.tasks:
            task_data = {
                'title': task.title,
                'description': task.description,
                'priority': task.priority.name,
                'deadline_date': task.deadline_date.strftime('%Y-%m-%d %H:%M') if task.deadline_date else None,
                'status': task.status.name,
                'created_date': task.created_date.strftime('%Y-%m-%d %H:%M'),
                'tags': list(task.tags)
            }
            tasks_data.append(task_data)

        try:
            with open(file_path, 'w') as json_file:
                json.dump(tasks_data, json_file, indent=4)
            print(f"Successfully saved {len(tasks_data)} tasks to JSON file")
        except IOError as e:
            raise IOError(f"Error saving to JSON file: {e}")

    def load_tasks_from_json(self, file_path):
        """
        Loads tasks from a JSON file.

        Args:
            file_path (str): The path to the file from where tasks should be loaded.

        Raises:
            IOError: If there's an error reading from the file.
            ValueError: If the JSON data is invalid.
        """
        print(f"Loading tasks from JSON file: {file_path}")
        try:
            with open(file_path, 'r') as json_file:
                tasks_data = json.load(json_file)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading from JSON file: {e}")

        self.tasks = []
        for task_data in tasks_data:
            task = Task(
                title=task_data['title'],
                description=task_data['description'],
                priority=TaskPriority[task_data['priority']],
                deadline_date=datetime.strptime(task_data['deadline_date'], '%Y-%m-%d %H:%M') if task_data['deadline_date'] else None,
            )
            task.status = TaskStatus[task_data['status']]
            task.created_date = datetime.strptime(task_data['created_date'], '%Y-%m-%d %H:%M')
            task.tags = set(task_data['tags'])
            self.tasks.append(task)
        print(f"Successfully loaded {len(self.tasks)} tasks from JSON file")

    def save_tasks_to_csv(self, file_path):
        """
        Saves the tasks to a CSV file.

        Args:
            file_path (str): The path to the file where tasks should be saved.

        Raises:
            IOError: If there's an error writing to the file.
        """
        print(f"Saving tasks to CSV file: {file_path}")
        try:
            with open(file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Title', 'Description', 'Priority', 'Deadline Date', 'Status', 'Created Date', 'Tags'])
                for task in self.tasks:
                    writer.writerow([
                        task.title,
                        task.description,
                        task.priority.name,
                        task.deadline_date.strftime('%Y-%m-%d %H:%M') if task.deadline_date else '',
                        task.status.name,
                        task.created_date.strftime('%Y-%m-%d %H:%M'),
                        ', '.join(task.tags)
                    ])
            print(f"Successfully saved {len(self.tasks)} tasks to CSV file")
        except IOError as e:
            raise IOError(f"Error saving to CSV file: {e}")

    def load_tasks_from_csv(self, file_path):
        """
        Loads tasks from a CSV file.

        Args:
            file_path (str): The path to the file from where tasks should be loaded.

        Raises:
            IOError: If there's an error reading from the file.
            ValueError: If the CSV data is invalid.
        """
        print(f"Loading tasks from CSV file: {file_path}")
        try:
            with open(file_path, 'r') as csv_file:
                reader = csv.DictReader(csv_file)

                self.tasks = []
                for row in reader:
                    task = Task(
                        title=row['Title'],
                        description=row['Description'],
                        priority=TaskPriority[row['Priority']],
                        deadline_date=row['Deadline Date']
                    )
                    task.status = TaskStatus[row['Status']]
                    task.created_date = datetime.strptime(row['Created Date'], '%Y-%m-%d %H:%M')
                    task.tags = set(row['Tags'].split(', '))
                    self.tasks.append(task)
        except IOError as e:
            raise IOError(f"Error loading from CSV file: {e}")
        except (ValueError, IndexError) as e:
            raise ValueError(f"Invalid CSV data: {e}")
        
    def file_task(self, task, file_path, format='json', overwrite=False, merge=False):
        """
        Add a new task to the file in the specified format.

        Args:
            task (object): The task to be added.
            format (str, optional): The file format to use. Defaults to 'json'.
            overwrite (bool, optional): Whether to replace an existing task. Defaults to False.
            merge (bool, optional): Whether to merge with an existing task. Defaults to False.

        Raises:
            ValueError: If the format is not recognized.
        """
        print(f"Filing task: {task.title}, Format: {format}, Overwrite: {overwrite}, Merge: {merge}")
        if format not in ['json', 'csv']:
            raise ValueError("Unrecognized format. Please use 'json' or 'csv'.")

        if format == 'json':
            self.load_tasks_from_json(file_path)
        elif format == 'csv':
            self.load_tasks_from_csv(file_path)

        existing_task = next((t for t in self.tasks if t.title == task.title), None)

        if existing_task:
            if overwrite:
                self.tasks.remove(existing_task)
                print(f"Task '{task.title}' has been replaced.")
            elif merge:
                existing_task.description = task.description
                existing_task.priority = task.priority
                existing_task.deadline_date = task.deadline_date
                existing_task.status = task.status
                existing_task.tags = task.tags
                print(f"Task '{task.title}' has been merged.")
            else:
                count = 1
                new_title = f"{task.title}_{count}"
                while any(t.title == new_title for t in self.tasks):
                    count += 1
                    new_title = f"{task.title}_{count}"
                task.title = new_title
                print(f"Task '{task.title}' has been added with a unique title.")
        else:
            print(f"Task '{task.title}' has been successfully added.")

        self.tasks.append(task)

        if format == 'json':
            self.save_tasks_to_json(file_path)
        elif format == 'csv':
            self.save_tasks_to_csv(file_path)
