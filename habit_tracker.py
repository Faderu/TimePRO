"""
Habit Tracker Module

This module provides classes for tracking habits, managing their progress, and setting reminders.

Classes:
    HabitCategory: An enumeration of possible habit categories (e.g., Health, Learning, Productivity).
    Habit: Represents a single habit, including attributes like name, target, category, history, and reminder settings.
    HabitTracker: Manages a collection of habits, allowing users to add, track, and report on their habits over time.

The module includes functionality to save and load habit data in both JSON and CSV formats,
allowing users to maintain their habit tracking information between sessions and choose their preferred file format.
"""

import datetime
import json
import csv
from enum import Enum

class HabitCategory(Enum):
    """Enum for defining habit categories.

    Attributes:
        HEALTH: Represents habits related to health.
        PRODUCTIVITY: Represents habits related to productivity.
        LEARNING: Represents habits related to learning.
        PERSONAL: Represents personal habits.
        OTHER: Represents habits that do not fall into the above categories.

      
    Example:
        >>> category = HabitCategory.HEALTH
        >>> print(category.name)
        HEALTH
        >>> print(category.value)
        1
        >>> if category == HabitCategory.HEALTH:
        ...     print("This is a health-related habit.")
        This is a health-related habit.
    """
    HEALTH = 1
    PRODUCTIVITY = 2
    LEARNING = 3
    PERSONAL = 4
    OTHER = 5

class Habit:
    """A class to represent an individual habit.

    Attributes:
        name (str): The name of the habit.
        target (str): The target or goal for the habit.
        category (HabitCategory): The category of the habit.
        history (dict): A dictionary to store the completion history of the habit.
        reminder_set (bool): A flag to indicate if a reminder is set for the habit.
    
    Methods:
        __init__(name, target, category): Initializes a new habit.
        _parse_date_input(date_str): Parses a date string to return a date object.
        mark_done(date_input): Marks the habit as done for the specified date.
        check_progress(start_date_input, end_date_input): Checks the progress of the habit.
        set_reminder(): Sets a reminder for the habit.
        get_streak(): Returns the current streak of consecutive days the habit has been completed.
        __str__(): Returns a string representation of the habit.
    """

    def __init__(self, name, target, category):
        self.name = name
        self.target = target
        self.category = category
        self.history = {}
        self.reminder_set = False

    def _parse_date_input(self, date_str):
        """Parses a date string to return a date object."""
        if date_str.lower() == "today":
            return datetime.date.today()
        elif date_str.lower() == "yesterday":
            return datetime.date.today() - datetime.timedelta(days=1)
        elif date_str.isdigit():
            return datetime.date.today() - datetime.timedelta(days=int(date_str))
        else:
            try:
                return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            except ValueError:
                return datetime.date.today()

    def mark_done(self, date_input="today"):
        """Marks the habit as done for the specified date.

        Args:
            date_input (str): The date for which to mark the habit as done (default is "today").

        Example:
            >>> habit = Habit("Exercise", "30 minutes daily", HabitCategory.HEALTH)
            >>> habit.mark_done("2024-10-01")
            >>> print(habit.history)
            {datetime.date(2024, 10, 1): True}
        """
        date = self._parse_date_input(date_input)
        self.history[date] = True

    def check_progress(self, start_date_input="today", end_date_input="today"):
        """Checks the progress of the habit between the specified dates.

        Returns:
            tuple: The number of completed days and total days in the given range.

        Example:
            >>> habit = Habit("Read", "1 chapter daily", HabitCategory.LEARNING)
            >>> habit.mark_done("2024-10-01")
            >>> habit.mark_done("2024-10-02")
            >>> completed, total = habit.check_progress("2024-10-01", "2024-10-02")
            >>> print(completed, total)
            (2, 2)
        """
        start_date = self._parse_date_input(start_date_input)
        end_date = self._parse_date_input(end_date_input)

        completed_days = sum(1 for i in range((end_date - start_date).days + 1)
                             if self.history.get(start_date + datetime.timedelta(days=i), False))
        total_days = (end_date - start_date).days + 1

        return completed_days, total_days

    def set_reminder(self):
        """Sets a reminder for the habit.

        Example:
            >>> habit = Habit("Meditate", "10 minutes daily", HabitCategory.HEALTH)
            >>> habit.set_reminder()
            >>> print(habit.reminder_set)
            True
        """
        self.reminder_set = True

    def get_streak(self):
        """Returns the current streak of consecutive days the habit has been completed.

        Example:
            >>> habit = Habit("Run", "5km daily", HabitCategory.HEALTH)
            >>> habit.mark_done("2024-10-01")
            >>> habit.mark_done("2024-10-02")
            >>> print(habit.get_streak())
            2
        """
        if not self.history:
            return 0
        
        today = datetime.date.today()
        streak = 0
        current_date = max(self.history)

        while current_date in self.history:
            streak += 1
            current_date -= datetime.timedelta(days=1)

        return streak

    def __str__(self):
        """Returns a string representation of the habit.

        Example:
            >>> habit = Habit("Yoga", "30 minutes daily", HabitCategory.HEALTH)
            >>> habit.mark_done("2024-10-01")
            >>> print(habit)
            Yoga - Target: 30 minutes daily, Category: HEALTH, Streak: 1
        """
        return f"{self.name} - Target: {self.target}, Category: {self.category.name}, Streak: {self.get_streak()}"

class HabitTracker:
    """A class to manage multiple habits and generate reports.

    Attributes:
        habits (list): A list to store instances of Habit.
    
    Methods:
        __init__(): Initializes a new habit tracker.
        add_habit(habit): Adds a new habit to the tracker.
        generate_habit_report(start_date, end_date): Generates a habit tracking report.
        _parse_date(date_string): Parses a date string to return a date object.
    """

    def __init__(self):
        self.habits = []

    def add_habit(self, habit):
        """Adds a new habit to the tracker.

        Args:
            habit (Habit): The habit to add.

        Example:
            >>> tracker = HabitTracker()
            >>> habit = Habit("Write", "500 words daily", HabitCategory.PRODUCTIVITY)
            >>> tracker.add_habit(habit)
            >>> print(len(tracker.habits))
            1
        """
        self.habits.append(habit)

    def generate_habit_report(self, start_date=None, end_date=None):
        """Generates a habit tracking report for the specified date range.

        Returns:
            str: A string containing the report.

        Example:
            >>> tracker = HabitTracker()
            >>> habit = Habit("Cook", "1 new recipe weekly", HabitCategory.PERSONAL)
            >>> tracker.add_habit(habit)
            >>> habit.mark_done("2024-10-01")
            >>> report = tracker.generate_habit_report("2024-10-01", "2024-10-02")
            >>> print(report)
            Habit Tracking Report
            =====================
            
            Date Range: 2024-10-01 to 2024-10-02
            
            Habits Summary:
              Cook (PERSONAL):
                Target: 1 new recipe weekly
                Completion Rate: 100.00% (1/2 days)
                Current Streak: 1 days
                Reminder Set: No
            
            Detailed Progress:
              Cook:
                2024-10-01: Completed
                2024-10-02: Not Completed
        """
        report = "Habit Tracking Report\n"
        report += "=====================\n\n"

        if start_date and end_date:
            report += f"Date Range: {start_date} to {end_date}\n\n"

        report += "Habits Summary:\n"
        for habit in self.habits:
            completed, total = habit.check_progress(start_date, end_date)
            completion_rate = (completed / total) * 100 if total > 0 else 0
            report += f"  {habit.name} ({habit.category.name}):\n"
            report += f"    Target: {habit.target}\n"
            report += f"    Completion Rate: {completion_rate:.2f}% ({completed}/{total} days)\n"
            report += f"    Current Streak: {habit.get_streak()} days\n"
            report += f"    Reminder Set: {'Yes' if habit.reminder_set else 'No'}\n\n"

        report += "Detailed Progress:\n"
        for habit in self.habits:
            report += f"  {habit.name}:\n"
            start = self._parse_date(start_date) if start_date else min(habit.history.keys(), default=datetime.date.today())
            end = self._parse_date(end_date) if end_date else max(habit.history.keys(), default=datetime.date.today())
            current = start
            while current <= end:
                status = "Completed" if habit.history.get(current, False) else "Not Completed"
                report += f"    {current}: {status}\n"
                current += datetime.timedelta(days=1)
            report += "\n"

        return report

    def _parse_date(self, date_string):
        """Parses a date string in "YYYY-MM-DD" format to return a date object.

        Args:
            date_string (str): The date string to parse.

        Returns:
            datetime.date: The parsed date object.

        Example:
            >>> tracker = HabitTracker()
            >>> date = tracker._parse_date("2024-10-01")
            >>> print(date)
            2024-10-01
        """
        return datetime.datetime.strptime(date_string, "%Y-%m-%d").date() if date_string else None
    
    def save_to_json(self, filename):
        """
        Saves the habit data to a JSON file.

        Args:
            filename (str): The name of the file to save the data to.

        Raises:
            IOError: If there's an error writing to the file.

        Example:
            >>> tracker = HabitTracker()
            >>> habit = Habit("Exercise", "30 minutes daily", HabitCategory.HEALTH)
            >>> tracker.add_habit(habit)
            >>> habit.mark_done("2023-05-01")
            >>> tracker.save_to_json("habits.json")
            # This will create a file 'habits.json' with the habit data
        """
        data = []
        for habit in self.habits:
            habit_data = {
                "name": habit.name,
                "target": habit.target,
                "category": habit.category.name,
                "history": {str(date): done for date, done in habit.history.items()},
                "reminder_set": habit.reminder_set
            }
            data.append(habit_data)

        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            raise IOError(f"Error saving to JSON file: {e}")

    def load_from_json(self, filename):
        """
        Loads habit data from a JSON file.

        Args:
            filename (str): The name of the file to load the data from.

        Raises:
            IOError: If there's an error reading from the file.
            ValueError: If the JSON data is invalid.

        Example:
            >>> tracker = HabitTracker()
            >>> tracker.load_from_json("habits.json")
            >>> print(tracker.generate_habit_report())
            # This will load the habits from 'habits.json' and print a report
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
        except IOError as e:
            raise IOError(f"Error loading from JSON file: {e}")

        self.habits = []
        for habit_data in data:
            habit = Habit(habit_data['name'], habit_data['target'], HabitCategory[habit_data['category']])
            habit.history = {datetime.datetime.strptime(date, "%Y-%m-%d").date(): done for date, done in habit_data['history'].items()}
            habit.reminder_set = habit_data['reminder_set']
            self.habits.append(habit)

    def save_to_csv(self, filename):
        """
        Saves the habit data to a CSV file.

        Args:
            filename (str): The name of the file to save the data to.

        Raises:
            IOError: If there's an error writing to the file.

        Example:
            >>> tracker = HabitTracker()
            >>> habit = Habit("Read", "1 chapter daily", HabitCategory.LEARNING)
            >>> tracker.add_habit(habit)
            >>> habit.mark_done("2023-05-01")
            >>> tracker.save_to_csv("habits.csv")
            # This will create a file 'habits.csv' with the habit data
        """
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Target', 'Category', 'History', 'Reminder Set'])
                for habit in self.habits:
                    history_str = ';'.join([f"{date}:{done}" for date, done in habit.history.items()])
                    writer.writerow([habit.name, habit.target, habit.category.name, history_str, habit.reminder_set])
        except IOError as e:
            raise IOError(f"Error saving to CSV file: {e}")

    def load_from_csv(self, filename):
        """
        Loads habit data from a CSV file.

        Args:
            filename (str): The name of the file to load the data from.

        Raises:
            IOError: If there's an error reading from the file.
            ValueError: If the CSV data is invalid.

        Example:
            >>> tracker = HabitTracker()
            >>> tracker.load_from_csv("habits.csv")
            >>> print(tracker.generate_habit_report())
            # This will load the habits from 'habits.csv' and print a report
        """
        try:
            with open(filename, 'r', newline='') as f:
                reader = csv.reader(f)
                next(reader)
                self.habits = []
                for row in reader:
                    name, target, category, history_str, reminder_set = row
                    habit = Habit(name, target, HabitCategory[category])
                    habit.history = {datetime.datetime.strptime(date, "%Y-%m-%d").date(): done == 'True'
                                     for date_done in history_str.split(';')
                                     for date, done in [date_done.split(':')]}
                    habit.reminder_set = reminder_set == 'True'
                    self.habits.append(habit)
        except IOError as e:
            raise IOError(f"Error loading from CSV file: {e}")
        except (ValueError, IndexError) as e:
            raise ValueError(f"Invalid CSV data: {e}")