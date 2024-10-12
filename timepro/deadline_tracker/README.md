# Deadline Tracker Module

---

### Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Class Overview](#class-overview)
4. [Detailed Class Descriptions and Usage](#detailed-class-descriptions-and-usage)

---

### Introduction

The Deadline Tracker Module is a Python tool designed to help users manage and track deadlines effectively. It provides classes and methods for creating deadlines, tracking their status, generating reports, and managing deadline data. This module is ideal for individuals, teams, or projects that need to keep track of multiple deadlines and improve overall task management.

---

### Features

- Create and manage deadlines with titles, descriptions, due dates, and priorities
- Track deadline status (pending, completed, or missed)
- Add tags and reminders to deadlines
- Filter deadlines by status, priority, or tags
- Get upcoming and overdue deadlines
- Calculate deadline completion rates
- Generate comprehensive deadline reports
- Save and load deadline data in JSON and CSV formats
- Flexible deadline management and analysis capabilities

---

### Class Overview

1. **Deadline**
   - Represents a single deadline with attributes such as `title`, `description`, `due_date`, `status`, `priority`, and `tags`.
   - Methods include:
     - Adding/removing reminders and tags
     - Marking deadlines as completed or missed
     - Checking if a deadline is overdue
     - Calculating remaining time

2. **DeadlineTracker**
   - Manages a collection of `Deadline` objects.
   - Methods include:
     - Adding/removing deadlines
     - Retrieving deadlines by different criteria (status, priority, tag)
     - Getting active, completed, and missed deadlines
     - Calculating deadline completion rate
     - Generating comprehensive deadline reports

3. **DeadlineFileManager**
   - Manages loading and saving of deadlines to/from JSON and CSV files.
   - Methods include:
     - Saving and loading deadlines data in JSON and CSV formats

---

### Detailed Class Descriptions and Usage

#### Deadline

The `Deadline` class is designed to represent individual deadlines with various attributes and methods for managing their status and details.

**Features in Deadline Class**
1. **Deadline Attributes:**
- `title` (str): The title of the deadline.
- `description` (str): A description of the deadline (optional).
- `due_date` (str): The date and time of the deadline.
- `reminders` (list): A list of `timedelta` objects for reminders.
- `status` (DeadlineStatus): The current status of the deadline (pending, completed, missed).
- `priority` (DeadlinePriority): The priority level of the deadline (low, medium, high).
- `created_date` (str): The date and time of creation.
- `tags` (set): A collection of tags associated with the deadline.

2. **Managing Deadline Status:**
- `mark_completed()`: Marks the deadline as completed.
- `mark_missed()`: Marks the deadline as missed.
- `is_overdue() -> bool`: Checks if the deadline has passed.

3. **Updating Deadline Details:**
- `add_reminder(reminder: timedelta)`: Adds a new reminder.
- `remove_reminder(reminder: timedelta)`: Removes a reminder from the deadline.
- `add_tag(tag: str)`: Adds a new tag.
- `remove_tag(tag: str)`: Removes a tag from the deadline.
- `time_remaining() -> timedelta`: Calculates the time remaining until the deadline.

4. **Displaying Deadline Representation:**
- `__str__() -> str`: Provides a string representation of the deadline.

**Usage for Deadline Class**
1. **Create a new deadline**
```python
from deadline_tracker import Deadline, DeadlineStatus, DeadlinePriority
deadline = Deadline(
    title="Project Presentation",
    description="Prepare and deliver project presentation",
    due_date="2024-10-15 14:00",
    priority=DeadlinePriority.HIGH
)
```

2. **Add a tag to the deadline**
```python
deadline.add_tag("project")
```

3. **Add a reminder to the deadline**
```python
from datetime import timedelta
deadline.add_reminder(timedelta(days=1))
```

4. **Mark the deadline as completed**
```python
deadline.mark_completed()
```

5. **Check if the deadline is overdue**
```python
is_overdue = deadline.is_overdue()
print(f"Is overdue: {is_overdue}")
```

---

#### DeadlineTracker

The `DeadlineTracker` class manages a collection of deadlines, allowing users to add, remove, and track the progress of their deadlines overall.

**Features in DeadlineTracker Class**
1. **DeadlineTracker Attributes:**
- `deadlines` (list): A list of `Deadline` objects being tracked.

2. **Adding and Removing Deadlines:**
- `add_deadline(deadline: Deadline)`: Adds a new deadline to the tracker.
- `remove_deadline(deadline: Deadline)`: Removes a deadline from the tracker.

3. **Retrieving Deadlines by Status:**
- `get_active_deadlines() -> list`: Retrieves all active (pending) deadlines.
- `get_completed_deadlines() -> list`: Retrieves all completed deadlines.
- `get_missed_deadlines() -> list`: Retrieves all missed deadlines.
- `get_deadlines_by_status(status: DeadlineStatus) -> list`: Retrieves all deadlines with a specific status.

4. **Retrieving Deadlines by Priority:**
- `get_deadlines_by_priority(priority: DeadlinePriority) -> list`: Retrieves all deadlines with a specific priority.

5. **Tracking Upcoming Deadlines:**
- `get_upcoming_deadlines(days: int = 7) -> list`: Retrieves deadlines due within a certain number of days.

6. **Checking Overdue Deadlines:**
- `get_overdue_deadlines() -> list`: Retrieves deadlines that have passed their due date.

7. **Calculating Deadline Statistics:**
- `get_completion_rate() -> float`: Calculates the overall deadline completion rate.

8. **Generating Deadline Report:**
- `generate_deadline_report() -> str`: Generates a comprehensive report on all tracked deadlines, including statistics and a detailed list of deadlines.

**Usage for DeadlineTracker Class**
1. **Create a new deadline tracker**
```python
from deadline_tracker import DeadlineTracker
tracker = DeadlineTracker()
```

2. **Add a deadline to the tracker**
```python
deadline = Deadline("Task 1", due_date="2024-10-15 14:00", priority=DeadlinePriority.HIGH)
tracker.add_deadline(deadline)
```

3. **Get all active deadlines**
```python
active_deadlines = tracker.get_active_deadlines()
print("Active deadlines:")
for deadline in active_deadlines:
    print(deadline)
```

4. **Get all completed deadlines**
```python
completed_deadlines = tracker.get_completed_deadlines()
print("Completed deadlines:")
for deadline in completed_deadlines:
    print(deadline)
```

5. **Get all deadlines with a specific status**
```python
deadlines_by_status = tracker.get_deadlines_by_status(DeadlineStatus.PENDING)
print("Deadlines by status:")
for deadline in deadlines_by_status:
    print(deadline)
```

6. **Get all deadlines with a specific priority**
```python
deadlines_by_priority = tracker.get_deadlines_by_priority(DeadlinePriority.HIGH)
print("Deadlines by priority:")
for deadline in deadlines_by_priority:
    print(deadline)
```

7. **Get all upcoming deadlines**
```python
upcoming_deadlines = tracker.get_upcoming_deadlines(days=7)
print("Upcoming deadlines (next 7 days):")
for deadline in upcoming_deadlines:
    print(deadline)
```

8. **Get all overdue deadlines**
```python
overdue_deadlines = tracker.get_overdue_deadlines()
print("Overdue deadlines:")
for deadline in overdue_deadlines:
    print(deadline)
```

9. **Get the overall deadline completion rate**
```python
completion_rate = tracker.get_completion_rate()
print(f"Completion rate: {completion_rate:.2f}%")
```

10. **Generate a comprehensive report of all deadlines**
```python
report = tracker.generate_deadline_report()
print(report)
```

---

#### DeadlineFileManager

The `DeadlineFileManager` class manages deadline data in JSON and CSV formats.

**Features in DeadlineFileManager Class**
1. **Attributes:**
- `deadlines` (list): A list of `Deadline` objects.

2. **Saving Data to JSON:**
- `save_to_json(filename: str)`: Saves the list of deadlines to a JSON file.
  - **Input**: Filename `str` to save the data.
  - **Output**: Generates a JSON file containing deadline data.
  - **Raises**: `IOError` if there's an error writing to the file.

3. **Loading Data from JSON:**
- `load_from_json(filename: str)`: Loads the list of deadlines from a JSON file.
  - **Input**: Filename `str` to load the data.
  - **Output**: Updates the `deadlines` list with `Deadline` objects.
  - **Raises**: `IOError` if there's an error reading the file; `ValueError` if the JSON data is invalid.

4. **Saving Data to CSV:**
- `save_to_csv(filename: str)`: Saves the list of deadlines to a CSV file.
  - **Input**: Filename `str` to save the data.
  - **Output**: Generates a CSV file containing deadline data.
  - **Raises**: `IOError` if there's an error writing to the file.

5. **Loading Data from CSV:**
- `load_from_csv(filename: str)`: Loads the list of deadlines from a CSV file.
  - **Input**: Filename `str` to load the data.
  - **Output**: Updates the `deadlines` list with `Deadline` objects.
  - **Raises**: `IOError` if there's an error reading the file; `ValueError` if the CSV data is invalid.

**Usage for DeadlineFileManager Class**
1. **Create a new deadline file manager**
```python
from deadline_tracker import DeadlineFileManager
manager = DeadlineFileManager()
```

2. **Save deadlines to a JSON file**
```python
manager.save_to_json("deadlines.json")
```

3. **Load deadlines from a JSON file**
```python
manager.load_from_json("deadlines.json")
```

4. **Save deadlines to a CSV file**
```python
manager.save_to_csv("deadlines.csv")
```

5. **Load deadlines from a CSV file**
```python
manager.load_from_csv("deadlines.csv")
```

---
