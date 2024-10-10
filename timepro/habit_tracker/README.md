# TimePRO
Tugas Package Library Algoritma dan Pemrograman

# Habit 
 Module

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
   - [HabitCategory](#habitcategory)
   - [Habit](#habit)
   - [HabitTracker](#habittracker)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The Habit Tracker Module is a Python tool designed to help users track and maintain their habits. It provides classes and methods for creating habits, tracking progress, setting reminders, and generating reports. This module is ideal for individuals looking to build positive routines, track daily achievements, and analyze their habit progress.

## Features

- Create and manage habits with targets and categories
- Track habit progress over time
- Mark habits as complete for specific dates
- Set reminders for habits
- Get habit streaks and completion rates
- Generate habit tracking reports
- Save and load habit data in JSON and CSV formats

## Installation

To use the Habit Tracker Module, simply copy the habit_tracker.py file into your project directory. The module uses only built-in Python libraries, so no additional dependencies are required.

## Usage

### HabitCategory

The HabitCategory class defines different categories of habits. You can assign a habit to one of these categories:

python
from habit_tracker import HabitCategory

category = HabitCategory.HEALTH
print(category.name)  # Outputs: HEALTH
print(category.value)  # Outputs: 1


### Habit

The Habit class allows you to create and track individual habits. It supports setting targets, tracking completion history, and managing reminders.

python
from habit_tracker import Habit, HabitCategory

habit = Habit("Exercise", "30 minutes daily", HabitCategory.HEALTH)
habit.mark_done("2024-10-01")
print(habit.get_streak())  # Outputs: 1


#### Key Methods

- mark_done(date_input="today"): Marks the habit as completed for the specified date.
- check_progress(start_date, end_date): Returns the number of completed and total days in the given range.
- get_streak(): Returns the current streak of consecutive days the habit has been completed.
- set_reminder(): Sets a reminder for the habit.

### HabitTracker

The HabitTracker class manages a collection of habits and provides methods for tracking progress and generating reports.

python
from habit_tracker import HabitTracker, Habit, HabitCategory

tracker = HabitTracker()
habit = Habit("Read", "1 chapter daily", HabitCategory.LEARNING)
tracker.add_habit(habit)

# Generate a report
print(tracker.generate_habit_report("2024-10-01", "2024-10-07"))


#### Key Methods

- add_habit(habit): Adds a new habit to the tracker.
- generate_habit_report(start_date, end_date): Generates a detailed report of habits over the specified date range.
- save_to_json(filename): Saves the habit data to a JSON file.
- load_from_json(filename): Loads habit data from a JSON file.
- save_to_csv(filename): Saves the habit data to a CSV file.
- load_from_csv(filename): Loads habit data from a CSV file.

## Examples

### Creating and Tracking Habits

python
from habit_tracker import HabitTracker, Habit, HabitCategory

tracker = HabitTracker()

# Add a new habit
habit = Habit("Exercise", "30 minutes daily", HabitCategory.HEALTH)
tracker.add_habit(habit)

# Mark the habit as done
habit.mark_done("2024-10-01")

# Get the habit streak
print(habit.get_streak())  # Outputs: 1


### Generating Reports

python
report = tracker.generate_habit_report("2024-10-01", "2024-10-07")
print(report)


### Saving and Loading Data

python
tracker.save_to_json("habits.json")
tracker.load_from_json("habits.json")
tracker.save_to_csv("habits.csv")
tracker.load_from_csv("habits.csv")


## Contributing

Contributions to the Habit Tracker Module are welcome! Please feel free to submit pull requests, create issues, or suggest new features to improve the module.

## License

This project is licensed under the MIT License. See the LICENSE file for details.