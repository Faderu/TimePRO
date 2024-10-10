# Task Management Module

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

The Task Management Module is a Python tool designed to help users create, manage, and track tasks effectively. It provides classes and methods for defining tasks, managing their status, generating reports, and handling task data in various formats. This module is ideal for individuals and teams looking to improve their task management and productivity.

## Features

- Create and manage tasks with titles, descriptions, deadlines, and priorities.
- Track task status (waiting, in progress, or completed).
- Add and remove tags associated with tasks.
- Check for overdue tasks and calculate remaining time.
- Filter tasks by status, priority, and tags.
- Generate comprehensive task reports.
- Save and load task data in JSON and CSV formats.
- Flexible task management and analysis capabilities.

## Installation

To use the Task Management Module, simply copy the `task_management.py` file into your project directory. The module requires Python 3.6 or higher and uses only built-in Python libraries, so no additional installation steps are necessary.

## Usage

### Task

The `Task` class represents a single task with attributes such as title, description, deadline, status, priority, and tags.

```python
from task_management import Task, TaskPriority, TaskStatus

task = Task(
    title="Complete Project Report",
    description="Finish the final report for the project",
    deadline_date="2024-10-15 12:00",
    priority=TaskPriority.HIGH
)
task.add_tag("report")
```

### TaskManager

The `TaskManager` class provides methods for managing multiple tasks and performing various analyses.

```python
from task_management import TaskManager, Task, TaskPriority

manager = TaskManager()
manager.add_task(Task("Task 1", deadline_date="2024-10-15 12:00", priority=TaskPriority.HIGH))
manager.add_task(Task("Task 2", deadline_date="2024-10-20 10:00", priority=TaskPriority.MEDIUM))

pending_tasks = manager.pending_tasks()
overdue_tasks = manager.get_overdue_tasks()
report = manager.generate_task_report()
```

### TaskFileManager

The `TaskFileManager` class handles saving and loading task data to and from JSON and CSV files.

```python
from task_management import TaskFileManager, TaskManager

manager = TaskManager()
# ... add tasks to manager ...

file_manager = TaskFileManager(manager.tasks)
file_manager.save_tasks_to_json("tasks.json")
file_manager.save_tasks_to_csv("tasks.csv")

loaded_file_manager = TaskFileManager()
loaded_file_manager.load_tasks_from_json("tasks.json")
```

## Examples

Here are some examples of how to use the Task Management Module:

1. Create and manage tasks:

```python
from task_management import TaskManager, Task, TaskPriority

manager = TaskManager()

# Add tasks
manager.add_task(Task("Submit Assignment", deadline_date="2024-11-01 17:00", priority=TaskPriority.HIGH))
manager.add_task(Task("Weekly Team Meeting", deadline_date="2024-10-15 10:00", priority=TaskPriority.MEDIUM))

# Get pending tasks
pending_tasks = manager.pending_tasks()
for task in pending_tasks:
    print(task)

# Mark a task as completed
task = manager.get_task("Submit Assignment")
if task:
    task.mark_completed()

# Generate a report
report = manager.generate_task_report()
print(report)
```

2. Filter and analyze tasks:

```python
from task_management import TaskManager, Task, TaskPriority

manager = TaskManager()
# ... add tasks to manager ...

# Get high-priority tasks
high_priority_tasks = manager.tasks_by_priority(TaskPriority.HIGH)
print("High priority tasks:")
for task in high_priority_tasks:
    print(task)

# Get upcoming tasks for the next 3 days
upcoming_tasks = manager.upcoming_tasks(days=3)
print("Upcoming tasks (next 3 days):")
for task in upcoming_tasks:
    print(task)

# Get overdue tasks
overdue_tasks = manager.get_overdue_tasks()
print("Overdue tasks:")
for task in overdue_tasks:
    print(task)
```

3. Generate and save a task report:

```python
from task_management import TaskManager, TaskFileManager

manager = TaskManager()
# ... add tasks to manager ...

# Generate a report
report = manager.generate_task_report()
print(report)

# Save tasks to a file
file_manager = TaskFileManager()
file_manager.save_tasks_to_json("task_report.json")
print("Task report saved to 'task_report.json'")
```

## Contributing

Contributions to the Task Management Module are welcome! Please feel free to submit pull requests, create issues, or suggest new features to improve the module.

## License

This project is licensed under the MIT License. See the LICENSE file for details.