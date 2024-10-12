# Habit Tracker Module

---

### Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Class Overview](#class-overview)
4. [Detailed And Usage](#detailed-class-descriptions-and-usage)

---

### Introduction

The Habit Tracker Module is a powerful tool designed to help users create, manage, and track their habits effectively. It allows users to set targets, categorize habits, monitor progress, and generate comprehensive reports. With the addition of file management features, users can save and load their habit data from JSON and CSV files, making it easy to maintain records and share habit data across different platforms.

---

### Features

- **Create and Manage Habits:** Add, update, and delete habits with descriptions, targets, categories, and frequencies.
- **Progress Tracking:** Monitor the progress of each habit based on completion history.
- **Streak Calculation:** Track the number of consecutive days a habit has been maintained.
- **Reminder System:** Set and manage reminders for habits to encourage consistency.
- **Categorization:** Group habits into categories for better organization.
- **Reporting:** Generate detailed reports on habit performance and progress.
- **File Management:** Save and load habit data to/from JSON and CSV formats.
- **Filtering and Sorting:** Retrieve habits by category, status, or upcoming due dates.

---

### Class Overview

1. **Habit**
   - Represents a single habit with attributes such as `title`, `category`, `frequency`, `target`, `progress`, `reminder`, and `created_date`.
   - Methods include:
     - Setting and removing targets
     - Updating progress
     - Getting habit status
     - Marking habits as complete for specific dates

2. **HabitCategory**
   - Defines categories for habits, such as Health, Productivity, etc.
   - Attributes include `name` and `description`.

3. **HabitReminder**
   - Manages reminders for habits.
   - Features include activating/deactivating reminders and updating reminder times and frequencies.

4. **HabitTracker**
   - Manages a collection of `Habit` objects.
   - Methods include:
     - Adding/removing habits
     - Retrieving habits by category
     - Checking habit streaks and progress
     - Generating habit reports
     - Setting reminders
     - Calculating completion rates and average progress

5. **HabitFileManager**
   - Manages loading and saving of habit data to/from JSON and CSV files.
   - Methods include:
     - Saving and loading habits data in JSON and CSV formats
     - Adding or updating individual habits in files

---

### Detailed Class Descriptions and Usage

#### Habit

The `Habit` class represents individual habits that users want to track and maintain.

**Features in Habit Class:**
1. **Habit Attributes:**
   - `title` (str): The title of the habit.
   - `category` (HabitCategory): The category of the habit.
   - `frequency` (str): How often the habit should be performed (e.g., daily, weekly).
   - `target` (int): The target number of completions.
   - `progress` (int): The number of times the habit has been completed.
   - `reminder` (bool): Whether a reminder is set for this habit.
   - `created_date` (date): The date the habit was created.

2. **Setting and Removing Targets:**
   - `set_target(target: int)`: Sets a new target for the habit.
   - `remove_target()`: Removes the current target.

3. **Updating Progress:**
   - `update_progress(value: int)`: Updates the progress of the habit.

4. **Checking Status:**
   - `get_status() -> str`: Returns the current status of the habit (e.g., not started, in progress, completed).

**Usage For Habir Class:**
1. **Create a new habit**
   ```python
   from timepro.habit_tracker import Habit, HabitCategory
   
   habit = Habit("Daily Exercise", "30 minutes of exercise daily", HabitCategory.HEALTH)
   ```

2. **Mark the habit as done**
   ```python
   habit.mark_done("2024-03-15")
   ```

3. **Check progress of the habit**
   ```python
   completed, total = habit.check_progress("2024-03-01", "2024-03-31")
   print(f"Completed {completed} out of {total} days")
   ```

4. **Set a reminder for the habit**
   ```python
   habit.set_reminder()
   ```

5. **Get the current streak**
   ```python
   streak = habit.get_streak()
   print(f"Current streak: {streak} days")
   ```

6. **Print habit information**
   ```python
   print(habit)

---

#### HabitTracker

The `HabitTracker` class manages a collection of habits and provides methods for tracking progress and generating reports.

**Features in HabitTracker Class:**
1. **HabitTracker Attributes:**
   - `habits` (list): A list of `Habit` objects being tracked.

2. **Adding and Removing Habits:**
   - `add_habit(habit: Habit)`: Adds a new habit to the tracker.
   - `remove_habit(habit: Habit)`: Removes a habit from the tracker.

3. **Grouping Habits by Category:**
   - `get_habits_by_category(category: HabitCategory) -> list`: Retrieves all habits in a specific category.

4. **Tracking Progress and Streaks:**
   - `get_habit_streak(habit: Habit) -> int`: Returns the current streak for a habit.
   - `check_progress(habit: Habit, start_date: str, end_date: str) -> tuple`: Checks the progress of a habit over a date range.

5. **Checking Overdue Habits:**
   - `get_overdue_habits() -> list`: Retrieves all habits that are past their due date.

6. **Managing Habit Reminders:**
   - `set_reminder(habit: Habit)`: Sets a reminder for a specific habit.

7. **Generating Habit Reports:**
   - `generate_habit_report(start_date: str, end_date: str) -> str`: Generates a comprehensive report on all tracked habits.

8. **Calculating Habit Statistics:**
   - `get_habit_completion_rate(habit: Habit) -> float`: Calculates the completion rate for a specific habit.
   - `get_average_habit_progress() -> float`: Calculates the average progress across all habits.

9. **Displaying Upcoming Habits:**
   - `get_upcoming_habits(days: int = 7) -> list`: Retrieves habits due within a specified number of days.

**Usage For HabitTracker Class:**
1. **Create a new habit tracker**
   ```python
   from timepro.habit_tracker import HabitTracker
   
   tracker = HabitTracker()
   ```

2. **Add a habit to the tracker**
   ```python
   tracker.add_habit(habit)
   ```

3. **Generate a habit report**
   ```python
   report = tracker.generate_habit_report("2024-03-01", "2024-03-31")
   print(report)
   ```

#### HabitFileManager

The `HabitFileManager` class manages habit data in JSON and CSV formats.

**Features in HabitFileManager Class:**
1. **Attributes:**
   - `habits` (list): A list of `Habit` objects.

2. **Saving Data to JSON:**
   - `save_to_json(filename: str)`: Saves the list of habits to a JSON file.

3. **Loading Data from JSON:**
   - `load_from_json(filename: str)`: Loads the list of habits from a JSON file.

4. **Saving Data to CSV:**
   - `save_to_csv(filename: str)`: Saves the list of habits to a CSV file.

5. **Loading Data from CSV:**
   - `load_from_csv(filename: str)`: Loads the list of habits from a CSV file.

6. **Adding or Updating Habits:**
   - `habit_file(habit: Habit, format='json', filename='habits.json', overwrite=False, merge=False)`: Adds or updates a habit in the file.

**Usage For HabitFileManager Class:**
1. **Create a new habit file manager**
   ```python
   from timepro.habit_tracker import HabitFileManager
   
   file_manager = HabitFileManager()
   ```

2. **Save habits to a JSON file**
   ```python
   file_manager.habits = [habit]
   file_manager.save_to_json("habits.json")
   ```

3. **Load habits from a JSON file**
   ```python
   file_manager.load_from_json("habits.json")
   ```

4. **Save habits to a CSV file**
   ```python
   file_manager.save_to_csv("habits.csv")
   ```

5. **Load habits from a CSV file**
   ```python
   file_manager.load_from_csv("habits.csv")
   ```

6. **Add or update a habit in a file**
   ```python
   new_habit = Habit("Read Books", "Read for 30 minutes daily", HabitCategory.LEARNING)
   file_manager.habit_file(new_habit, format='json', filename='habits.json', overwrite=True)
---
