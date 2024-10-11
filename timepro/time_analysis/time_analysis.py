import json
import csv
from datetime import datetime, timedelta, date
from collections import defaultdict
from enum import Enum

class TimeCategory(Enum):
    """
    Enum for time entry categories.

    Attributes:
        WORK (int): The time entry belongs to work.
        BREAK (int): The time entry belongs to a break.
        HABIT (int): The time entry belongs to a habit.
        PERSONAL (int): The time entry belongs to personal time.
        OTHER (int): The time entry belongs to other categories.
    """
    WORK = 1
    BREAK = 2
    HABIT = 3
    PERSONAL = 4
    OTHER = 5

class TimeEntry:
    """
    A class to represent a time entry for analysis.

    Attributes:
        start_time (datetime): The start time of the entry.
        end_time (datetime): The end time of the entry.
        category (TimeCategory): The category of the time entry.
        description (str): A description of the time entry.
        tags (set): A set of tags associated with the time entry.
    """

    def __init__(self, start_time, end_time, category, description="", duration=None, tags=set()):
        """
        Initializes a TimeEntry object.

        Args:
            start_time (datetime): The start time of the entry.
            end_time (datetime): The end time of the entry.
            category (TimeCategory): The category of the time entry.
            description (str, optional): A description of the time entry. Defaults to "".
            
        """
        self.start_time = self._parse_time(start_time)
        self.end_time = self._parse_time(end_time)
        self.category = category
        self.description = description
        self.duration = self.end_time - self.start_time
        self.tags = set()

    def _parse_time(self, time_input):
        """
        Parse various time input formats.

        Args:
            time_input (datetime or str): The time input to parse.

        Returns:
            datetime: The parsed time.

        Raises:
            ValueError: If the time format is invalid.
            TypeError: If the time input is not a datetime object or a string.
        """
        if isinstance(time_input, datetime):
            return time_input
        elif isinstance(time_input, str):
            try:
                return datetime.strptime(time_input, "%Y-%m-%d %H:%M")
            except ValueError:
                try:
                    return datetime.strptime(time_input, "%H:%M").replace(
                        year=datetime.now().year,
                        month=datetime.now().month,
                        day=datetime.now().day
                    )
                except ValueError:
                    raise ValueError("Invalid time format. Use 'YYYY-MM-DD HH:MM' or 'HH:MM'.")
        else:
            raise TypeError("Time must be a datetime object or a string.")

    def duration(self):
        """
        Calculate the duration of the time entry.

        Returns:
            timedelta: The duration of the time entry.
        """
        print("Calculating duration")
        return self.end_time - self.start_time

    def add_tag(self, tag):
        """
        Add a tag to the time entry.

        Args:
            tag (str): The tag to add.

        Raises:
            ValueError: If the tag is None.
        """
        print(f"Adding tag: {tag}")
        if tag is None:
            raise ValueError("Tag cannot be None")
        self.tags.add(tag.lower())

    def remove_tag(self, tag):
        """
        Remove a tag from the time entry.

        Args:
            tag (str): The tag to remove.

        Raises:
            ValueError: If the tag is None.
        """
        print(f"Removing tag: {tag}")
        if tag is None:
            raise ValueError("Tag cannot be None")
        self.tags.discard(tag.lower())

    def __str__(self):
        return f"{self.category.name}: {self.start_time.strftime('%Y-%m-%d %H:%M')} - {self.end_time.strftime('%H:%M')} ({self.duration})"

class TimeAnalyzer:
    """
    A class to analyze time usage based on time entries.

    Attributes:
        entries (list): A list of TimeEntry objects.
    """

    def __init__(self):
        self.entries = []

    def add_entry(self, start_time, end_time, category, description=""):
        """
        Add a new time entry for analysis.

        Args:
            start_time (datetime or str): The start time of the entry.
            end_time (datetime or str): The end time of the entry.
            category (TimeCategory): The category of the time entry.
            description (str, optional): A description of the time entry. Defaults to "".
        """
        print(f"Adding entry: {start_time} - {end_time}, {category}, {description}")
        entry = TimeEntry(start_time, end_time, category, description)
        self.entries.append(entry)

    def remove_entry(self, start_time):
        """
        Remove a time entry by its start time.

        Args:
            start_time (datetime or str): The start time of the entry to remove.
        """
        print(f"Removing entry: {start_time}")
        start_time = self._parse_time_input(start_time)
        self.entries = [entry for entry in self.entries if entry.start_time != start_time]

    def get_entry(self, start_time):
        """
        Get a time entry by its start time.

        Args:
            start_time (datetime or str): The start time of the entry to get.

        Returns:
            TimeEntry: The time entry with the specified start time, or None if not found.
        """
        print(f"Getting entry: {start_time}")
        start_time = self._parse_time_input(start_time)
        return next((entry for entry in self.entries if entry.start_time == start_time), None)

    def update_entry(self, start_time, **kwargs):
        """
        Update a time entry with given attributes.

        Args:
            start_time (datetime or str): The start time of the entry to update.
            **kwargs: The attributes to update.

        Raises:
            ValueError: If the entry with the specified start time is not found.
        """
        print(f"Updating entry: {start_time}")
        start_time = self._parse_time_input(start_time)
        entry = self.get_entry(start_time)
        if entry:
            for key, value in kwargs.items():
                if key in ['start_time', 'end_time']:
                    setattr(entry, key, self._parse_time_input(value))
                elif hasattr(entry, key):
                    setattr(entry, key, value)
        else:
            raise ValueError(f"Entry with start time '{start_time}' not found.")

    def _parse_time_input(self, time_input):
        """
        Parse time input for flexible user input.

        Args:
            time_input (datetime or str): The time input to parse.

        Returns:
            datetime: The parsed time.

        Raises:
            ValueError: If the time format is invalid.
            TypeError: If the time input is not a datetime object or a string.
        """
        if isinstance(time_input, datetime):
            return time_input
        elif isinstance(time_input, str):
            try:
                return datetime.strptime(time_input, "%Y-%m-%d %H:%M")
            except ValueError:
                try:
                    return datetime.strptime(time_input, "%Y-%m-%d")
                except ValueError:
                    try:
                        dt = datetime.strptime(time_input, "%H:%M")
                        return dt.replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
                    except ValueError:
                        raise ValueError("Invalid time format. Use 'YYYY-MM-DD HH:MM', 'YYYY-MM-DD', or 'HH:MM'.")
        else:
            raise TypeError("Time must be a datetime object or a string.")

    def get_total_time_by_category(self, start_date=None, end_date=None):
        """
        Calculate the total time spent on each category within a date range.

        Args:
            start_date (datetime or str, optional): The start date of the range. Defaults to None.
            end_date (datetime or str, optional): The end date of the range. Defaults to None.

        Returns:
            dict: A dictionary with categories as keys and total times as values.
        """
        print("Calculating total time by category")
        start_date = self._parse_time_input(start_date) if start_date else None
        end_date = self._parse_time_input(end_date) if end_date else None
        total_time = defaultdict(timedelta)
        for entry in self.entries:
            if (not start_date or entry.start_time >= start_date) and \
               (not end_date or entry.end_time <= end_date):
                total_time[entry.category] += entry.duration
        return dict(total_time)
        
    def get_productivity_score(self, productive_categories, date):
        """
        Calculate a productivity score based on time spent in productive categories.

        Args:
            productive_categories (list): A list of productive categories.
            date (datetime or str, optional): The date to calculate the score for. Defaults to None.

        Returns:
            float: The productivity score.
        """
        print("Calculating productivity score")
        date = self._parse_time_input(date).date() if date else None
        total_time = timedelta()
        productive_time = timedelta()

        for entry in self.entries:
            if date is None or entry.start_time.date() == date:
                duration = entry.duration
                total_time += duration
                if entry.category in productive_categories:
                    productive_time += duration

        if total_time == timedelta():
            return 0
        return productive_time.total_seconds() / total_time.total_seconds()

    def list_entries(self, filter_by_category=None):
        """
        List all entries or filter by category.

        Args:
            filter_by_category (TimeCategory, optional): The category to filter by. Defaults to None.

        Returns:
            list: A list of TimeEntry objects.
        """
        print("Listing entries")
        if filter_by_category:
            return [entry for entry in self.entries if entry.category == filter_by_category]
        return self.entries

    def entries_by_date_range(self, start_date=None, end_date=None):
        """
        Get entries within a specified date range.

        Args:
            start_date (datetime or str, optional): The start date of the range. Defaults to None.
            end_date (datetime or str, optional): The end date of the range. Defaults to None.

        Returns:
            list: A list of TimeEntry objects.
        """
        print("Filtering entries by date range")
        start_date = self._parse_time_input(start_date) if start_date else datetime.min
        end_date = self._parse_time_input(end_date) if end_date else datetime.max
        return [entry for entry in self.entries if start_date <= entry.start_time <= end_date]

    def get_entries_by_tag(self, tag):
        """
        Get entries filtered by a specific tag.

        Args:
            tag (str): The tag to filter by.

        Returns:
            list: A list of TimeEntry objects.
        """
        print("Filtering entries by tag")
        return [entry for entry in self.entries if tag.lower() in entry.tags]

    def generate_time_report(self, start_date=None, end_date=None):
        """
        Generate a report of time entries.

        Args:
            start_date (datetime or str, optional): The start date of the range. Defaults to None.
            end_date (datetime or str, optional): The end date of the range. Defaults to None.

        Returns:
            str: A report of time entries.
        """
        start_date = self._parse_time_input(start_date) if start_date else None
        end_date = self._parse_time_input(end_date) if end_date else None

        report = "Time Analysis Report\n"
        report += "=====================\n\n"

        filtered_entries = self.entries_by_date_range(start_date, end_date)

        report += f"Total Entries: {len(filtered_entries)}\n\n"

        report += "Time by Category:\n"
        category_totals = self.get_total_time_by_category(start_date, end_date)
        for category, duration in category_totals.items():
            report += f"  {category.name}: {duration}\n"

        report += "\nDetailed Entry List:\n"
        for entry in filtered_entries:
            report += f"\n{entry}\n"
            report += f"  Description: {entry.description}\n"
            report += f"  Tags: {', '.join(entry.tags) if entry.tags else 'None'}\n"

        return report

class TimeFileManager:
    def __init__(self):
        self.time_entries = []

    def save_to_json(self, file_path):
        """
        Saves the time entries to a JSON file.

        Args:
            file_path (str): The path to the file where time entries should be saved.

        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump([{
                    'start_time': entry.start_time.isoformat(),
                    'end_time': entry.end_time.isoformat(),
                    'category': entry.category.name,
                    'description': entry.description,
                    'tags': list(entry.tags)
                } for entry in self.time_entries], json_file, indent=2)
            print(f"Data successfully saved to {file_path}")
        except IOError as e:
            print(f"Error saving to JSON file: {e}")


    def load_from_json(self, file_path):
        """
        Loads time entries from a JSON file.

        Args:
            file_path (str): The path to the file from where time entries should be loaded.

        Returns:
            list: A list of TimeEntry objects.

        Raises:
            IOError: If there's an error reading from the file.
            ValueError: If the JSON data is invalid.
        """
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                self.time_entries = []
                for entry_data in data:
                    entry = TimeEntry(
                        start_time=datetime.fromisoformat(entry_data['start_time']),
                        end_time=datetime.fromisoformat(entry_data['end_time']),
                        category=TimeCategory[entry_data['category']],
                        description=entry_data['description'],
                        tags=set(entry_data['tags'])
                    )
                    self.time_entries.append(entry)
                print(f"Data successfully loaded from {file_path}")
                return self.time_entries
        except IOError as e:
            print(f"Error loading from JSON file: {e}")
        except (ValueError, KeyError) as e:
            print(f"Invalid JSON data: {e}")
        return []

    def save_to_csv(self, file_path):
        """
        Saves the time entries to a CSV file.

        Args:
            file_path (str): The path to the file where time entries should be saved.

        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Category', 'Start Time', 'End Time', 'Duration', 'Description', 'Tags'])
                for entry in self.time_entries:
                    writer.writerow([
                        entry.category.name,
                        entry.start_time.strftime('%Y-%m-%d %H:%M'),
                        entry.end_time.strftime('%Y-%m-%d %H:%M'),
                        str(entry.end_time - entry.start_time),
                        entry.description,
                        ', '.join(entry.tags)
                    ])
            print(f"Data successfully saved to {file_path}")
        except IOError as e:
            print(f"Error saving to CSV file: {e}")

    def load_from_csv(self, file_path):
        """
        Loads time entries from a CSV file.

        Args:
            file_path (str): The path to the file from where time entries should be loaded.

        Returns:
            list: A list of TimeEntry objects.

        Raises:
            IOError: If there's an error reading from the file.
            ValueError: If the CSV data is invalid.
        """
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.time_entries = []
                for row in reader:
                    entry = TimeEntry(
                        start_time=datetime.strptime(row['Start Time'], '%Y-%m-%d %H:%M'),
                        end_time=datetime.strptime(row['End Time'], '%Y-%m-%d %H:%M'),
                        category=TimeCategory[row['Category']],
                        description=row['Description'],
                        tags=set(row['Tags'].split(', ')) if row['Tags'] else set()
                    )
                    self.time_entries.append(entry)
            print(f"Data successfully loaded from {file_path}")
            return self.time_entries
        except IOError as e:
            print(f"Error loading from CSV file: {e}")
        except (ValueError, KeyError) as e:
            print(f"Invalid CSV data: {e}")
        return []


    def file_time_entry(self, time_entry, format='json', filename='time_entries.json', overwrite=False, merge=False):
        """
        Add or update a time entry in the file in the specified format.

        Args:
            time_entry (TimeEntry): The time entry to be added.
            format (str, optional): The file format to use. Defaults to 'json'.
            filename (str, optional): The file name. Defaults to 'time_entries.json'.
            overwrite (bool, optional): Whether to replace an existing time entry. Defaults to False.
            merge (bool, optional): Whether to merge with an existing time entry. Defaults to False.

        Raises:
            ValueError: If the format is not recognized or if there's a conflict with existing entries.
        """
        if format not in ['json', 'csv']:
            raise ValueError("Unrecognized format. Please use 'json' or 'csv'.")

        try:
            if format == 'json':
                self.load_from_json(filename)
            elif format == 'csv':
                self.load_from_csv(filename)
        except FileNotFoundError:
            pass

        existing_entry = next((entry for entry in self.time_entries if entry.start_time == time_entry.start_time), None)

        if existing_entry:
            if overwrite:
                existing_entry.__dict__.update(time_entry.__dict__)
                print(f"Time entry at {time_entry.start_time} has been replaced.")
            elif merge:
                existing_entry.end_time = max(existing_entry.end_time, time_entry.end_time)
                existing_entry.tags.update(time_entry.tags)
                print(f"Time entry at {time_entry.start_time} has been merged.")
            else:
                raise ValueError("Time entry already exists. Use overwrite or merge to update.")
        else:
            self.time_entries.append(time_entry)
            print(f"Time entry at {time_entry.start_time} has been successfully added.")

        if format == 'json':
            self.save_to_json(filename)
        elif format == 'csv':
            self.save_to_csv(filename)
