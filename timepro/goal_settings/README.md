# Goal Settings Module

---

### Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Class Overview](#class-overview)
4. [Detailed And Usage](#detailed-class-descriptions-and-usage)

---

### Introduction

The Goal Settings is a tool designed to help users set, manage, and track their goals effectively. It allows users to break down goals into smaller milestones, set priorities, and track progress over time. With the addition of file management features, users can save and load their goals from JSON and CSV files, making it easy to maintain records and share goal data across different platforms.

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
   - Methods include:
     - Adding/removing milestones and tags
     - Checking progress
     - Marking goals as completed or abandoned
     - Calculating remaining days
     - Checking if the goal is overdue

2. **Milestone**
   - Represents a subtask within a goal, with attributes like `description`, `target_date`, `completed`, and `completion_date`.
   - Methods include:
     - Marking as completed
     - Checking if overdue

3. **GoalTracker**
   - Manages a collection of `Goal` objects.
   - Methods include:
     - Adding/removing goals
     - Retrieving goals by different criteria (status, priority, tag, progress)
     - Getting active, completed, and overdue goals
     - Calculating goal completion rate and average progress
     - Generating comprehensive goal reports

4. **GoalFileManager**
   - Manages loading and saving of goals to/from JSON and CSV files.
   - Methods include:
     - Saving and loading goals data in JSON and CSV formats
     - Adding or updating individual goals in files

---

### Detailed Class Descriptions And Usage

#### Goal

The `Goal` class is designed to help users set, track, and achieve their goals by breaking them down into smaller steps (milestones). Users can manage various aspects of goals, including status, priority, and progress.

**Fiture In Goal Class**
1. **Goal Attributes:**
- `title` (str): The title of the goal.
- `description` (str): A description of the goal.
- `target_date` (date): The target date for achieving the goal.
- `milestones` (list): A list of `Milestone` objects representing the steps toward the goal.
- `status` (GoalStatus): The current status of the goal (e.g., NOT_STARTED, IN_PROGRESS, COMPLETED, ABANDONED).
- `priority` (GoalPriority): The priority level of the goal (e.g., LOW, MEDIUM, HIGH).
- `created_date` (date): The date the goal was created.
- `tags` (set): A collection of tags associated with the goal for easier searching.

2. **Adding and Removing Milestones:**
- `add_milestone(milestone: Milestone)`: Adds a milestone to the goal and updates the status.
- `remove_milestone(milestone: Milestone)`: Removes a milestone from the goal and updates the status.

3. **Managing Tags:**
- `add_tag(tag: str)`: Adds a new tag to the goal.
- `remove_tag(tag: str)`: Removes a tag from the goal.

4. **Calculating Progress:**
- `get_progress() -> float`: Calculates the percentage of progress based on the number of completed milestones.

5. **Checking Overdue and Status:**
- `is_overdue() -> bool`: Checks whether the goal has passed the target date.
- `mark_completed()`: Marks the goal as completed.
- `mark_abandoned()`: Marks the goal as abandoned.

6. **Calculating Remaining Days:**
- `get_remaining_days() -> int`: Calculates the number of days remaining until the target date.

**Usage For Goal Class**
1. **Create a new goal**
```python
from timepro.goal_setting import Goal
goal = Goal("Learn Python", "Learn the basics of Python programming", "2024-03-31")
```

2. **Add a milestone to the goal**
```python
milestone = Milestone("Complete Python basics course")
goal.add_milestone(milestone)
```

3. **Mark the milestone as completed**
```python
milestone.mark_completed()
```
4. **Get the progress of the goal**
```python
progress = goal.get_progress()
print(f"Progress: {progress}%")
```

5. **Get the remaining days until the target date**
```python
remaining_days = goal.get_remaining_days()
print(f"Remaining days: {remaining_days}")
```

6. **Check if the goal is overdue**
```python
is_overdue = goal.is_overdue()
print(f"Is overdue: {is_overdue}")
```

---

#### Milestone

The `Milestone` class defines milestones as specific steps needed to achieve a goal. Each milestone has attributes that allow users to track its progress.

**Fiture In Milestone Class**
1. **Milestone Attributes:**
- `description` (str): The description of the milestone.
- `target_date` (date): The target date for completing the milestone.
- `completed` (bool): Status indicating whether the milestone has been completed or not.
- `completion_date` (date): The date when the milestone was completed.

2. **Marking Milestone:**
- `mark_completed(completion_date: date)`: Marks the milestone as completed and stores the completion date.

3. **Checking Milestone Overdue:**
- `is_overdue() -> bool`: Checks whether the milestone has passed the target date.

4. **Displaying Milestone Representation:**
- `__str__() -> str`: Provides a clear string representation of the milestone, including its status and target date.

**Usage For Milestone Class**
1. **Create a new milestone**
```python
from timepro.goal_setting import Milestone
milestone = Milestone("Complete Python basics course", "2024-03-15")
```

2. **Mark the milestone as completed**
```python
milestone.mark_completed()
```

3. **Check if the milestone is overdue**
```python
is_overdue = milestone.is_overdue()
print(f"Is overdue: {is_overdue}")
```
---

#### GoalTracker

The `GoalTracker` class manages a collection of goals, allowing users to add, remove, and track the progress of their goals overall.

**Fiture In GoalTracker Class**
1. **GoalTracker Attributes:**
- `goals` (list): A list of `Goal` objects being tracked.

2. **Adding and Removing Goals:**
- `add_goal(goal: Goal)`: Adds a new goal to the tracker.
- `remove_goal(goal: Goal)`: Removes a goal from the tracker.

3. **Grouping Goals by Criteria:**
- `get_active_goals() -> list`: Retrieves all active goals (not completed or abandoned).
- `get_completed_goals() -> list`: Retrieves all completed goals.
- `get_goals_by_status(status: GoalStatus) -> list`: Retrieves all goals with a specific status.
- `get_goals_by_priority(priority: GoalPriority) -> list`: Retrieves all goals with a specific priority.
- `get_goals_by_tag(tag: str) -> list`: Retrieves all goals with a specific tag.
- `get_goals_by_progress(min_progress: float, max_progress: float) -> list`: Retrieves goals within a specific progress range.
- `get_overdue_goals() -> list`: Retrieves all goals that are overdue.

4. **Tracking Upcoming Milestones:**
- `get_upcoming_milestones(days: int = 7) -> list`: Retrieves all milestones due within a certain number of days.

5. **Calculating Goal Statistics:**
- `get_goal_completion_rate() -> float`: Calculates the overall goal completion rate.
- `get_average_goal_progress() -> float`: Calculates the average progress among all active goals.

6. **Generating Goal Report:**
- `generate_goal_report() -> str`: Generates a comprehensive report on all tracked goals, including statistics and a detailed list of goals.

**Usage For GoalTracker Class**
1. **Create a new goal tracker**
```python
from timepro.goal_setting import GoalTracker, GoalStatus, GoalPriority
tracker = GoalTracker()
```

2. **Add a goal to the tracker**
```python
goal = Goal("Learn Python", "Learn the basics of Python programming", "2024-03-31")
tracker.add_goal(goal)
```

3. **Get all active goals**
```python
active_goals = tracker.get_active_goals()
print("Active goals:")
for goal in active_goals:
    print(goal)
```

4. **Get all completed goals**
```python
completed_goals = tracker.get_completed_goals()
print("Completed goals:")
for goal in completed_goals:
    print(goal)
```

5. **Get all goals with a specific status**
```python
goals_by_status = tracker.get_goals_by_status(GoalStatus.IN_PROGRESS)
print("Goals by status:")
for goal in goals_by_status:
    print(goal)
```

6. **Get all goals with a specific priority**
```python
goals_by_priority = tracker.get_goals_by_priority(GoalPriority.HIGH)
print("Goals by priority:")
for goal in goals_by_priority:
    print(goal)
```

7. **Get all goals with a specific tag**
```python
goals_by_tag = tracker.get_goals_by_tag("python")
print("Goals by tag:")
for goal in goals_by_tag:
    print(goal)
```

8. **Get all goals within a specific progress range**
```python
goals_by_progress = tracker.get_goals_by_progress(50, 100)
print("Goals by progress:")
for goal in goals_by_progress:
    print(goal)
```

9. **Get all overdue goals**
```python
overdue_goals = tracker.get_overdue_goals()
print("Overdue goals:")
for goal in overdue_goals:
    print(goal)
```

10. **Get all upcoming milestones**
```python
upcoming_milestones = tracker.get_upcoming_milestones()
print("Upcoming milestones:")
for goal, milestone in upcoming_milestones:
    print(f"[{goal.title}] {milestone.description} - Due: {milestone.target_date}")
```

11. **Get the overall goal completion rate**
```python
completion_rate = tracker.get_goal_completion_rate()
print(f"Completion rate: {completion_rate}%")
```

12. Get the average progress across all active goals
```python
average_progress = tracker.get_average_goal_progress()
print(f"Average progress: {average_progress}%")
````

13. Generate a comprehensive report of all goals
```python
report = tracker.generate_goal_report()
print(report)
```
---

#### GoalFileManager

The `GoalFileManager` class manages goal data in JSON and CSV formats.

**Features In GoalFileManager Class**
1. **Attributes:**
- `json_filename` (str): The name of the file for saving data in JSON format.
- `csv_filename` (str): The name of the file for saving data in CSV format.
- `goals` (list): A list of `Goal` objects.

2. **Saving Data to JSON:**
- `save_to_json()`: Saves the list of goals to a JSON file.

3. **Loading Data from JSON:**
- `load_from_json()`: Loads the list of goals from a JSON file.

4. **Saving Data to CSV:**
- `save_to_csv()`: Saves the list of goals to a CSV file.

5. **Loading Data from CSV:**
- `load_from_csv()`: Loads the list of goals from a CSV file.

6. **Adding or Updating Goals:**
- `file_goal(goal: Goal, format='json', overwrite=False, merge=False)`: Adds or updates a goal in the file.

**Usage For GoalFileManager Class**
1. **Create a new goal file manager**
```python
from timepro.goal_setting import GoalFileManager
manager = GoalFileManager("goals.json", "goals.csv")
```

2. **Save goals to a JSON file**
```python
manager.save_to_json()
```

3. **Load goals from a JSON file**
```python
manager.load_from_json()
```

4. **Save goals to a CSV file**
```python
manager.save_to_csv()
```

5. **Load goals from a CSV file**
```python
manager.load_from_csv()
```

6. **Add or update a goal in the file**
```python
goal = Goal("Learn Python", "Learn the basics of Python programming", "2024-03-31")
manager.file_goal(goal, format="json", overwrite=True, merge=False)
```
---