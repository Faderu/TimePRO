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
        _init_(name, target, category): Initializes a new habit.
        _parse_date_input(date_str): Parses a date string to return a date object.
        mark_done(date_input): Marks the habit as done for the specified date.
        check_progress(start_date_input, end_date_input): Checks the progress of the habit.
        set_reminder(): Sets a reminder for the habit.
        get_streak(): Returns the current streak of consecutive days the habit has been completed.
        _str_(): Returns a string representation of the habit.
    """

    def _init_(self, name, target, category, history={}, reminder_set=False):
        print(f"Initializing habit: {name}")
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
        """
        Marks the habit as done for the specified date.

        Args:
            date_input (str): The date for which to mark the habit as done (default is "today").
        """
        print(f"Marking {self.name} as done for {date_input}")
        date = self._parse_date_input(date_input)
        self.history[date] = True

    def check_progress(self, start_date_input="today", end_date_input="today"):
        """
        Checks the progress of the habit between the specified dates.

        Returns:
            tuple: The number of completed days and total days in the given range.
        """
        print(f"Checking progress of {self.name} between {start_date_input} and {end_date_input}")
        start_date = self._parse_date_input(start_date_input)
        end_date = self._parse_date_input(end_date_input)

        completed_days = sum(1 for i in range((end_date - start_date).days + 1)
                             if self.history.get(start_date + datetime.timedelta(days=i), False))
        total_days = (end_date - start_date).days + 1

        return completed_days, total_days

    def set_reminder(self):
        """Sets a reminder for the habit."""
        print(f"Setting reminder for {self.name}")
        self.reminder_set = True

    def get_streak(self):
        """Returns the current streak of consecutive days the habit has been completed."""
        if not self.history:
            return 0
        
        today = datetime.date.today()
        streak = 0
        current_date = max(self.history)

        while current_date in self.history:
            streak += 1
            current_date -= datetime.timedelta(days=1)

        print(f"Streak of {self.name} is {streak} days")
        return streak

    def _str_(self):
        """Returns a string representation of the habit."""
        return f"{self.name} - Target: {self.target}, Category: {self.category.name}, Streak: {self.get_streak()}"

class HabitTracker:
    """
    A class to manage multiple habits and generate reports.

    Attributes:
        habits (list): A list to store instances of Habit.
    
    Methods:
        _init_(): Initializes a new habit tracker.
        add_habit(habit): Adds a new habit to the tracker.
        generate_habit_report(start_date, end_date): Generates a habit tracking report.
        _parse_date(date_string): Parses a date string to return a date object.
    """

    def _init_(self):
        print("Initializing habit tracker")
        self.habits = []

    def add_habit(self, habit):
        """
        Adds a new habit to the tracker.

        Args:
            habit (Habit): The habit to add.
        """
        print(f"Adding habit: {habit.name}")
        self.habits.append(habit)

    def generate_habit_report(self, start_date=None, end_date=None):
        """Generates a habit tracking report for the specified date range.

        Returns:
            str: A string containing the report.
        """
        print(f"Generating habit report between {start_date} and {end_date}")
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
        """
        return datetime.datetime.strptime(date_string, "%Y-%m-%d").date() if date_string else None
    
class HabitFileManager:
    def _init_(self):
        print("Initializing habit file manager")
        self.habits = []

    def save_to_json(self, filename):
        """
        Saves the habit data to a JSON file.

        Args:
            filename (str): The name of the file to save the data to.

        Raises:
            IOError: If there's an error writing to the file.
        """
        print(f"Saving habits to JSON file: {filename}")
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
            print(f"Habits successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving to JSON file: {e}")
            raise IOError(f"Error saving to JSON file: {e}")

    def load_from_json(self, filename):
        """
        Loads habit data from a JSON file.

        Args:
            filename (str): The name of the file to load the data from.

        Raises:
            IOError: If there's an error reading from the file.
            ValueError: If the JSON data is invalid.
        """
        print(f"Loading habits from JSON file: {filename}")
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            print(f"Habits successfully loaded from {filename}")
        except IOError as e:
            print(f"Error loading from JSON file: {e}")
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
        """
        print(f"Saving habits to CSV file: {filename}")
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Target', 'Category', 'History', 'Reminder Set'])
                for habit in self.habits:
                    history_str = ';'.join([f"{date}:{done}" for date, done in habit.history.items()])
                    writer.writerow([habit.name, habit.target, habit.category.name, history_str, habit.reminder_set])
            print(f"Habits successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving to CSV file: {e}")
            raise IOError(f"Error saving to CSV file: {e}")

    def load_from_csv(self, filename):
        """
        Loads habit data from a CSV file.

        Args:
            filename (str): The name of the file to load the data from.

        Raises:
            IOError: If there's an error reading from the file.
            ValueError: If the CSV data is invalid.
        """
        print(f"Loading habits from CSV file: {filename}")
        try:
            with open(filename, 'r', newline='') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header row
                self.habits = []
                for row in reader:
                    name, target, category, history_str, reminder_set = row
                    habit = Habit(name, target, HabitCategory[category])
                    habit.history = {datetime.datetime.strptime(date, "%Y-%m-%d").date(): done == 'True'
                                     for date_done in history_str.split(';')
                                     for date, done in [date_done.split(':')]}
                    habit.reminder_set = reminder_set == 'True'
                    self.habits.append(habit)
            print(f"Habits successfully loaded from {filename}")
        except IOError as e:
            print(f"Error loading from CSV file: {e}")
            raise IOError(f"Error loading from CSV file: {e}")
        except (ValueError, IndexError) as e:
            print(f"Invalid CSV data: {e}")
            raise ValueError(f"Invalid CSV data: {e}")

    def habit_file(self, habit, format='json', filename='habits.json', overwrite=False, merge=False):
        """
        Add or update a habit in the file in the specified format.

        Args:
            habit (Habit): The habit to be added.
            format (str, optional): The file format to use. Defaults to 'json'.
            filename (str, optional): The file name. Defaults to 'habits.json'.
            overwrite (bool, optional): Whether to replace an existing habit. Defaults to False.
            merge (bool, optional): Whether to merge with an existing habit. Defaults to False.

        Raises:
            ValueError: If the format is not recognized.
        """
        print(f"Handling habit file operation with format: {format}, filename: {filename}")
        if format not in ['json', 'csv']:
            raise ValueError("Unrecognized format. Please use 'json' or 'csv'.")

        if format == 'json':
            try:
                self.load_from_json(filename)
            except FileNotFoundError:
                print(f"File {filename} not found, starting with an empty habit list.")
        elif format == 'csv':
            try:
                self.load_from_csv(filename)
            except FileNotFoundError:
                print(f"File {filename} not found, starting with an empty habit list.")

        existing_habit = next((h for h in self.habits if h.name == habit.name), None)

        if existing_habit:
            print(f"Habit '{habit.name}' found, updating...")
            if overwrite:
                existing_habit.target = habit.target
                existing_habit.category = habit.category
                existing_habit.history = habit.history
                existing_habit.reminder_set = habit.reminder_set
                print(f"Habit '{habit.name}' updated with overwrite.")
            elif merge:
                existing_habit.history.update(habit.history)
                existing_habit.reminder_set = habit.reminder_set
                print(f"Habit '{habit.name}' updated with merge.")
            else:
                raise ValueError("Habit already exists. Use overwrite or merge to update.")
        else:
            print(f"Adding new habit '{habit.name}' to the list.")
            self.habits.append(habit)

        if format == 'json':
            self.save_to_json(filename)
        elif format == 'csv':
            self.save_to_csv(filename)
