# Task Management Module

---

### Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Class Overview](#class-overview)
4. [Detailed And Usage](#detailed-class-descriptions-and-usage)

---

### Introduction

The Task Management Module is a Python tool designed to help users create, manage, and track tasks effectively. It provides classes and methods for defining tasks, managing their status, generating reports, and handling task data in various formats. This module is ideal for individuals and teams looking to improve their task management and productivity.

---

### Features

- Create and manage tasks with titles, descriptions, deadlines, and priorities.
- Track task status (waiting, in progress, or completed).
- Add and remove tags associated with tasks.
- Check for overdue tasks and calculate remaining time.
- Filter tasks by status, priority, and tags.
- Generate comprehensive task reports.
- Save and load task data in JSON and CSV formats.
- Flexible task management and analysis capabilities.

---

### Class Overview

1. **Task**
   - Represents a single task with attributes such as `title`, `description`, `status`, `priority`, `deadline_date`, `created_date`, and `tags`.
   - Methods include:
     - Adding/removing tags
     - Checking if overdue
     - Calculating remaining time
     - Marking tasks as completed
     - Updating task status

2. **TaskManager**
   - Manages a collection of `Task` objects.
   - Methods include:
     - Adding/removing tasks
     - Retrieving tasks by different criteria (status, priority, tag)
     - Getting pending and overdue tasks
     - Generating task reports

3. **TaskFileManager**
   - Manages loading and saving of tasks to/from JSON and CSV files.
   - Methods include:
     - Saving and loading tasks data in JSON and CSV formats
     - Adding or updating individual tasks in files

---

### Detailed Class Descriptions And Usage

#### Task

The `Task` class is designed to help users create and manage individual tasks with various attributes and methods for tracking their progress.

**Features In Task Class**
1. **Task Attributes:**
- `title` (str): The title of the task.
- `description` (str): A description of the task.
- `priority` (TaskPriority): The priority level of the task (e.g., LOW, MEDIUM, HIGH).
- `deadline_date` (datetime): The deadline for completing the task.
- `status` (TaskStatus): The current status of the task (e.g., WAITING, IN_PROGRESS, COMPLETED).
- `created_date` (datetime): The date the task was created.
- `tags` (set): A collection of tags associated with the task for easier searching.

2. **Initializing a Task:**
- `__init__(self, title, description="", priority=TaskPriority.MEDIUM, deadline_date=None)`: Initializes a new Task instance with the given attributes.

3. **Marking Task as Completed:**
- `mark_completed()`: Marks the task as completed.

4. **Updating Task Status:**
- `update_status(self, status)`: Updates the task's status with a new status.

5. **Managing Tags:**
- `add_tag(self, tag)`: Adds a new tag to the task.
- `remove_tag(self, tag)`: Removes a tag from the task.

6. **Checking Overdue Status:**
- `is_overdue(self)`: Checks whether the task has passed its deadline.

7. **Calculating Remaining Time:**
- `time_remaining(self)`: Calculates the time remaining until the deadline.

8. **String Representation:**
- `__str__(self)`: Returns a string representation of the task.

**Usage For Task Class**
1. **Create a new task**
```python
from timepro.task_management import Task, TaskPriority
task = Task("Complete Project Report", "Finish the final report for the project", TaskPriority.HIGH, "2024-03-31")
```

2. **Add a tag to the task**
```python
task.add_tag("report")
```

3. **Mark the task as completed**
```python
task.mark_completed()
```

4. **Check if the task is overdue**
```python
is_overdue = task.is_overdue()
print(f"Is overdue: {is_overdue}")
```

5. **Get the remaining time for the task**
```python
remaining_time = task.time_remaining()
print(f"Remaining time: {remaining_time}")
```

---

#### TaskManager

The `TaskManager` class manages a collection of tasks, allowing users to add, remove, update, and filter tasks based on various criteria.

**Features In TaskManager Class**
1. **TaskManager Attributes:**
- `tasks` (list): A list of `Task` objects being managed.

2. **Adding and Removing Tasks:**
- `add_task(self, task)`: Adds a new task to the manager.
- `remove_task(self, title)`: Removes a task from the manager by its title.

3. **Retrieving Tasks:**
- `get_task(self, title)`: Retrieves a task by its title.
- `list_tasks(self, filter_by_status=None)`: Lists all tasks or filters by status.
- `upcoming_tasks(self, days=7)`: Retrieves tasks due within a certain number of days.
- `tasks_by_priority(self, priority)`: Retrieves tasks with a specific priority.
- `pending_tasks(self)`: Retrieves all pending (non-completed) tasks.
- `get_overdue_tasks(self)`: Retrieves all overdue tasks.
- `get_tasks_by_tag(self, tag)`: Retrieves tasks with a specific tag.

4. **Updating Tasks:**
- `update_task(self, title, **kwargs)`: Updates a task's attributes.

5. **Generating Task Report:**
- `generate_task_report(self)`: Generates a comprehensive report of all tasks.

**Usage For TaskManager Class**
1. **Create a new task manager**
```python
from task_management import TaskManager, Task, TaskPriority
manager = TaskManager()
```

2. **Add a task to the manager**
```python
task = Task("Complete Project Report", "Finish the final report for the project", TaskPriority.HIGH, "2024-03-31")
manager.add_task(task)
```

3. **Get all pending tasks**
```python
pending_tasks = manager.pending_tasks()
print("Pending tasks:")
for task in pending_tasks:
    print(task)
```

4. **Get all tasks with a specific priority**
```python
high_priority_tasks = manager.tasks_by_priority(TaskPriority.HIGH)
print("High priority tasks:")
for task in high_priority_tasks:
    print(task)
```

5. **Get all overdue tasks**
```python
overdue_tasks = manager.get_overdue_tasks()
print("Overdue tasks:")
for task in overdue_tasks:
    print(task)
```

6. **Generate a comprehensive report of all tasks**
```python
report = manager.generate_task_report()
print(report)
```

---

#### TaskFileManager

The `TaskFileManager` class manages task data in JSON and CSV formats.

**Features In TaskFileManager Class**
1. **Attributes:**
- `tasks` (list): A list of `Task` objects.

2. **Saving Data to JSON:**
- `save_tasks_to_json(file_path: str)`: Saves the list of tasks to a JSON file.

3. **Loading Data from JSON:**
- `load_tasks_from_json(file_path: str)`: Loads the list of tasks from a JSON file.

4. **Saving Data to CSV:**
- `save_tasks_to_csv(file_path: str)`: Saves the list of tasks to a CSV file.

5. **Loading Data from CSV:**
- `load_tasks_from_csv(file_path: str)`: Loads the list of tasks from a CSV file.

6. **Adding or Updating Tasks:**
- `file_task(task: Task, format='json', overwrite=False, merge=False)`: Adds or updates a task in the file.

**Usage For TaskFileManager Class**
1. **Create a new task file manager**
```python
from timepro.task_management import TaskFileManager
file_manager = TaskFileManager()
```

2. **Save tasks to a JSON file**
```python
file_manager.save_tasks_to_json(file_path="tasks.json")
```

3. **Load tasks from a JSON file**
```python
file_manager.load_tasks_from_json(file_path="tasks.json")
```

4. **Save tasks to a CSV file**
```python
file_manager.save_tasks_to_csv(file_path="tasks.csv")
```

5. **Load tasks from a CSV file**
```python
file_manager.load_tasks_from_csv(file_path="tasks.csv")
```

6. **Add or update a task in the file**
```python
task = Task("Complete Project Report", "Finish the final report for the project", TaskPriority.HIGH, "2024-03-31")
file_manager.file_task(task, file_path="tasks.json", format="json", overwrite=True, merge=False)
```
---
