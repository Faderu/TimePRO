**README - Goal Tracker Application**

---

### Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Class Overview](#class-overview)
4. [Usage](#usage)
5. [File Management](#file-management)
6. [Installation](#installation)
7. [Contributing](#contributing)
8. [License](#license)

---

### Introduction

The **Goal Tracker Application** is a tool designed to help users set, manage, and track their goals effectively. It allows users to break down goals into smaller milestones, set priorities, and track progress over time. With the addition of file management features, users can save and load their goals from JSON and CSV files, making it easy to maintain records and share goal data across different platforms.

---

### Features

- **Create and Manage Goals:** Add, update, and delete goals with descriptions, target dates, priorities, and tags.
- **Milestone Management:** Add milestones to goals, mark them as completed, and set due dates.
- **Progress Tracking:** Track the progress of each goal based on its milestones.
- **Status and Priority Handling:** Update goal statuses (e.g., *In Progress*, *Completed*, *Abandoned*) and set priorities (e.g., *High*, *Medium*, *Low*).
- **Goal Reports:** Generate reports summarizing goal data, including completion rates and upcoming milestones.
- **File Management:** Save and load goals to/from JSON and CSV formats.
- **Filtering and Sorting:** Filter goals by status, priority, tag, or progress percentage.

---

### Class Overview

1. **Goal**
   - Represents a single goal with attributes such as `title`, `description`, `status`, `priority`, `target_date`, `created_date`, and `tags`.
   - Methods include adding/removing milestones and tags, checking progress, and marking goals as completed or abandoned.

2. **Milestone**
   - Represents a subtask within a goal, with attributes like `description`, `target_date`, and `completed`.
   - Can be marked as completed and checked for overdue status.

3. **GoalTracker**
   - Manages a collection of `Goal` objects.
   - Methods include adding/removing goals, retrieving goals by different criteria, and generating reports.

4. **GoalFileManager**
   - Manages loading and saving of goals to/from JSON and CSV files.
   - Methods include `save_to_json`, `load_from_json`, `save_to_csv`, and `load_from_csv`.

---

### Usage

```python
# Initialize the GoalTracker
tracker = GoalTracker()

# Create a new goal
goal = Goal(title="Learn Python", description="Master the basics of Python programming", target_date="2024-12-31", priority=GoalPriority.HIGH)

# Add milestones to the goal
goal.add_milestone(Milestone(description="Complete Python Basics Course", target_date="2024-11-01"))
goal.add_milestone(Milestone(description="Build a Small Python Project", target_date="2024-12-01"))

# Add goal to the tracker
tracker.add_goal(goal)

# Save goals to a JSON file
file_manager = GoalFileManager("goals.json", "goals.csv")
file_manager.goals = tracker.goals
file_manager.save_to_json()
```

This snippet shows how to create a goal, add milestones, and save the goal data to a file using the `GoalFileManager` class.

---

### File Management

The **GoalFileManager** class allows users to save and load goals from JSON and CSV files. It provides the following methods:

- **save_to_json:** Saves the current list of goals to a JSON file.
- **load_from_json:** Loads goals from a JSON file and updates the `goals` attribute.
- **save_to_csv:** Saves the current list of goals to a CSV file.
- **load_from_csv:** Loads goals from a CSV file and updates the `goals` attribute.

For example, to load goals from a JSON file:

```python
file_manager.load_from_json()
print(file_manager.goals)  # Print the list of goals loaded from the file
```

---




