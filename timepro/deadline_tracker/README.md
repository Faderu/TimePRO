# Deadline Tracker Module

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Deadline](#deadline)
   - [DeadlineTracker](#deadlinetracker)
   - [DeadlineFileManager](#deadlinefilemanager)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The Deadline Tracker Module is a Python tool designed to help users manage and track deadlines effectively. It provides classes and methods for creating deadlines, tracking their status, generating reports, and managing deadline data. This module is ideal for individuals, teams, or projects that need to keep track of multiple deadlines and improve overall task management.

## Features

- Create and manage deadlines with titles, descriptions, due dates, and priorities
- Track deadline status (pending, completed, or missed)
- Add tags and reminders to deadlines
- Filter deadlines by status, priority, or tags
- Get upcoming and overdue deadlines
- Calculate deadline completion rates
- Generate comprehensive deadline reports
- Save and load deadline data in JSON and CSV formats
- Flexible deadline management and analysis capabilities

## Installation

To use the Deadline Tracker Module, simply copy the `deadline_tracker.py` file into your project directory. The module requires Python 3.6 or higher and uses only built-in Python libraries, so no additional installation steps are necessary.

## Usage

### Deadline

The `Deadline` class represents a single deadline with attributes such as title, description, due date, status, priority, and tags.

```python
from deadline_tracker import Deadline, DeadlineStatus, DeadlinePriority

deadline = Deadline(
    title="Project Presentation",
    description="Prepare and deliver project presentation",
    due_date="2024-10-15 14:00",
    priority=DeadlinePriority.HIGH
)
deadline.add_tag("project")
deadline.add_reminder(timedelta(days=1))
```

### DeadlineTracker

The `DeadlineTracker` class provides methods for managing multiple deadlines and performing various analyses.

```python
from deadline_tracker import DeadlineTracker, Deadline, DeadlinePriority

tracker = DeadlineTracker()
tracker.add_deadline(Deadline("Task 1", due_date="2024-10-15 14:00", priority=DeadlinePriority.HIGH))
tracker.add_deadline(Deadline("Task 2", due_date="2024-10-20 10:00", priority=DeadlinePriority.MEDIUM))

active_deadlines = tracker.get_active_deadlines()
upcoming_deadlines = tracker.get_upcoming_deadlines(days=7)
completion_rate = tracker.get_completion_rate()
report = tracker.generate_deadline_report()
```

### DeadlineFileManager

The `DeadlineFileManager` class handles saving and loading deadline data to and from JSON and CSV files.

```python
from deadline_tracker import DeadlineFileManager, DeadlineTracker

tracker = DeadlineTracker()
# ... add deadlines to tracker ...

file_manager = DeadlineFileManager(tracker.deadlines)
file_manager.save_to_json("deadlines.json")
file_manager.save_to_csv("deadlines.csv")

loaded_file_manager = DeadlineFileManager()
loaded_file_manager.load_from_json("deadlines.json")
```

## Examples

Here are some examples of how to use the Deadline Tracker Module:

1. Create and manage deadlines:

```python
from deadline_tracker import DeadlineTracker, Deadline, DeadlinePriority

tracker = DeadlineTracker()

# Add deadlines
tracker.add_deadline(Deadline("Report Submission", due_date="2024-11-01 17:00", priority=DeadlinePriority.HIGH))
tracker.add_deadline(Deadline("Team Meeting", due_date="2024-10-15 10:00", priority=DeadlinePriority.MEDIUM))

# Get active deadlines
active_deadlines = tracker.get_active_deadlines()
for deadline in active_deadlines:
    print(deadline)

# Mark a deadline as completed
deadline = tracker.get_active_deadlines()[0]
deadline.mark_completed()

# Get completion rate
completion_rate = tracker.get_completion_rate()
print(f"Completion rate: {completion_rate:.2f}%")
```

2. Filter and analyze deadlines:

```python
from deadline_tracker import DeadlineTracker, Deadline, DeadlinePriority

tracker = DeadlineTracker()
# ... add deadlines to tracker ...

# Get high priority deadlines
high_priority = tracker.get_deadlines_by_priority(DeadlinePriority.HIGH)
print("High priority deadlines:")
for deadline in high_priority:
    print(deadline)

# Get upcoming deadlines for the next 3 days
upcoming = tracker.get_upcoming_deadlines(days=3)
print("Upcoming deadlines (next 3 days):")
for deadline in upcoming:
    print(deadline)

# Get overdue deadlines
overdue = tracker.get_overdue_deadlines()
print("Overdue deadlines:")
for deadline in overdue:
    print(deadline)
```

3. Generate and save a deadline report:

```python
from deadline_tracker import DeadlineTracker, DeadlineFileManager

tracker = DeadlineTracker()
# ... add deadlines to tracker ...

# Generate a report
report = tracker.generate_deadline_report()
print(report)

# Save deadlines to a file
file_manager = DeadlineFileManager(tracker.deadlines)
file_manager.save_to_json("deadline_report.json")
print("Deadline report saved to 'deadline_report.json'")
```

## Contributing

Contributions to the Deadline Tracker Module are welcome! Please feel free to submit pull requests, create issues, or suggest new features to improve the module.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
