Berikut adalah file `README.md` yang sesuai dengan modul yang telah Anda berikan:

```markdown
# Deadline Tracker Module

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Task](#task)
   - [TaskManager](#taskmanager)
   - [TaskFileManager](#taskfilemanager)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The Deadline Tracker Module is a Python tool designed to help users manage and track tasks effectively. It provides classes and methods for creating tasks, tracking their status, generating reports, and managing task data. This module is ideal for individuals, teams, or projects that need to keep track of multiple tasks and improve overall task management.

## Features

- Create and manage tasks with titles, descriptions, due dates, and priorities.
- Track task status (waiting, in progress, completed).
- Add tags to tasks.
- Filter tasks by status, priority, or tags.
- Get upcoming and overdue tasks.
- Calculate task completion rates.
- Generate comprehensive task reports.
- Save and load task data in JSON and CSV formats.

## Installation

To use the Task Manager Module, simply copy the `task_manager.py` file into your project directory. The module requires Python 3.6 or higher and uses only built-in Python libraries, so no additional installation steps are necessary.

## Usage

### Task

The `Task` class represents a single task with attributes such as title, description, due date, status, priority, and tags.

```python
from task_manager import Task, TaskPriority, TaskStatus

task = Task(
    title="Prepare Presentation",
    description="Prepare slides for the upcoming project presentation",
    deadline_date="2024-10-15 14:00",
    priority=TaskPriority.HIGH
)
task.add_tag("project")
```

### TaskManager

The `TaskManager` class provides methods for managing multiple tasks and performing various analyses.

```python
from task_manager import TaskManager, Task, TaskPriority

manager = TaskManager()
manager.add_task(Task("Task 1", deadline_date="2024-10-15 14:00", priority=TaskPriority.HIGH))
manager.add_task(Task("Task 2", deadline_date="2024-10-20 10:00", priority=TaskPriority.MEDIUM))

# Get tasks
tasks = manager.list_tasks()
upcoming_tasks = manager.upcoming_tasks(days=7)
overdue_tasks = manager.get_overdue_tasks()
```

### TaskFileManager

The `TaskFileManager` class handles saving and loading task data to and from JSON and CSV files.

```python
from task_manager import TaskFileManager, TaskManager

manager = TaskManager()
# ... add tasks to manager ...

file_manager = TaskFileManager(manager.tasks)
file_manager.save_tasks_to_json("tasks.json")
file_manager.save_tasks_to_csv("tasks.csv")

# Load tasks from file
loaded_manager = TaskFileManager()
loaded_manager.load_tasks_from_json("tasks.json")
```

## Examples

Here are some examples of how to use the Task Manager Module:

1. **Create and manage tasks**:

```python
from task_manager import TaskManager, Task, TaskPriority

manager = TaskManager()

# Add tasks
manager.add_task(Task("Report Submission", deadline_date="2024-11-01 17:00", priority=TaskPriority.HIGH))
manager.add_task(Task("Team Meeting", deadline_date="2024-10-15 10:00", priority=TaskPriority.MEDIUM))

# Get active tasks
active_tasks = manager.list_tasks()
for task in active_tasks:
    print(task)

# Mark a task as completed
task = active_tasks[0]
task.mark_completed()

# Get completion rate
completion_rate = manager.generate_task_report()
print(completion_rate)
```

2. **Filter and analyze tasks**:

```python
from task_manager import TaskManager, Task, TaskPriority

manager = TaskManager()
# ... add tasks to manager ...

# Get high priority tasks
high_priority = manager.tasks_by_priority(TaskPriority.HIGH)
print("High priority tasks:")
for task in high_priority:
    print(task)

# Get upcoming tasks for the next 3 days
upcoming = manager.upcoming_tasks(days=3)
print("Upcoming tasks (next 3 days):")
for task in upcoming:
    print(task)

# Get overdue tasks
overdue = manager.get_overdue_tasks()
print("Overdue tasks:")
for task in overdue:
    print(task)
```

3. **Generate and save a task report**:

```python
from task_manager import TaskManager, TaskFileManager

manager = TaskManager()
# ... add tasks to manager ...

# Generate a report
report = manager.generate_task_report()
print(report)

# Save tasks to a file
file_manager = TaskFileManager(manager.tasks)
file_manager.save_tasks_to_json("task_report.json")
print("Task report saved to 'task_report.json'")
```

## Contributing

Contributions to the Task Manager Module are welcome! Please feel free to submit pull requests, create issues, or suggest new features to improve the module.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```

Let me know if you need further modifications or additions to this file!