import json
import csv
from datetime import datetime, timedelta
from enum import Enum

class DeadlineStatus(Enum):
    """
    Enum for representing the status of a deadline.

    Attributes:
        PENDING (int): Indicates that the deadline is still active and pending.
        COMPLETED (int): Indicates that the deadline has been successfully completed.
        MISSED (int): Indicates that the deadline was missed.
    """
    PENDING = 0
    COMPLETED = 1
    MISSED = 2

class DeadlinePriority(Enum):
    """
    Enum for representing the priority level of a deadline.

    Attributes:
        LOW (int): Represents a low-priority deadline.
        MEDIUM (int): Represents a medium-priority deadline.
        HIGH (int): Represents a high-priority deadline.
    """
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Deadline:
    """
    A class to represent a deadline.

    Attributes:
        title (str): The title of the deadline.
        description (str): A description of the deadline.
        due_date (str): The due date and time of the deadline as a string.
        reminders (list): A list of timedelta objects representing when reminders should be sent.
        status (DeadlineStatus): The current status of the deadline.
        priority (DeadlinePriority): The priority level of the deadline.
        created_date (str): The date and time when the deadline was created as a string.
        tags (set): A set of tags associated with the deadline.
    """

    def __init__(self, title, description="", due_date=None, reminders=[], status=DeadlineStatus.PENDING, priority=DeadlinePriority.MEDIUM, created_date=None, tags=[]):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.reminders = [timedelta(days=1), timedelta(hours=1)]
        self.status = DeadlineStatus.PENDING
        self.priority = priority
        self.created_date = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.tags = set()
        print(f"Deadline '{self.title}' created.")

    def add_reminder(self, reminder):
        """
        Add a reminder to the deadline.

        Args:
            reminder (timedelta): The reminder to add.
        """
        self.reminders.append(reminder)
        print(f"Reminder added to deadline '{self.title}'.")

    def remove_reminder(self, reminder):
        """
        Remove a reminder from the deadline.

        Args:
            reminder (timedelta): The reminder to remove.
        """
        self.reminders.remove(reminder)
        print(f"Reminder removed from deadline '{self.title}'.")

    def add_tag(self, tag):
        """
        Add a tag to the deadline.

        Args:
            tag (str): The tag to add.
        """
        self.tags.add(tag.lower())
        print(f"Tag '{tag}' added to deadline '{self.title}'.")

    def remove_tag(self, tag):
        """
        Remove a tag from the deadline.

        Args:
            tag (str): The tag to remove.
        """
        self.tags.discard(tag.lower())
        print(f"Tag '{tag}' removed from deadline '{self.title}'.")

    def mark_completed(self):
        """
        Mark the deadline as completed.
        """
        self.status = DeadlineStatus.COMPLETED
        print(f"Deadline '{self.title}' marked as completed.")

    def mark_missed(self):
        """
        Mark the deadline as missed.
        """
        self.status = DeadlineStatus.MISSED
        print(f"Deadline '{self.title}' marked as missed.")

    def is_overdue(self):
        """
        Check if the deadline is overdue.

        Returns:
            bool: True if the deadline is overdue, False otherwise.
        """
        if self.due_date:
            due_date_time = datetime.strptime(self.due_date, '%Y-%m-%d %H:%M')
            is_overdue = datetime.now() > due_date_time and self.status == DeadlineStatus.PENDING
            print(f"Checked if deadline '{self.title}' is overdue: {is_overdue}.")
            return is_overdue
        return False

    def time_remaining(self):
        """
        Calculate the time remaining until the deadline.

        Returns:
        timedelta: The time remaining until the deadline, or None if no due date is set.
        """
        if self.due_date:
            due_date_time = datetime.strptime(self.due_date, '%Y-%m-%d %H:%M')
            remaining_time = due_date_time - datetime.now()
            print(f"Time remaining for deadline '{self.title}': {remaining_time}.")
            return remaining_time
        print(f"No due date set for deadline '{self.title}'.")
        return None

    def to_dict(self):
        """
        Convert the Deadline object to a dictionary for JSON serialization.

        Returns:
            dict: A dictionary representation of the Deadline object.
        """
        print(f"Converting deadline '{self.title}' to dictionary.")
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'reminders': [str(r.total_seconds()) for r in self.reminders],
            'status': self.status.name,
            'priority': self.priority.name,
            'created_date': self.created_date,
            'tags': list(self.tags)
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Deadline object from a dictionary.

        Args:
            data (dict): A dictionary containing deadline data.

        Returns:
            Deadline: A new Deadline object.
        """
        print(f"Creating deadline from dictionary data.")
        deadline = cls(data['title'], data['description'], data['due_date'], DeadlinePriority[data['priority']])
        deadline.reminders = [timedelta(seconds=float(r)) for r in data['reminders']]
        deadline.status = DeadlineStatus[data['status']]
        deadline.created_date = data['created_date']
        deadline.tags = set(data['tags'])
        return deadline

    def __str__(self):
        return f"{self.title} - Due: {self.due_date}, Status: {self.status.name}, Priority: {self.priority.name}"

class DeadlineTracker:
    """
    A class to track multiple deadlines.

    Attributes:
        deadlines (list): A list of Deadline objects.
    """

    def __init__(self):
        self.deadlines = []
        print("Deadline Tracker initialized.")

    def add_deadline(self, deadline):
        """
        Add a new deadline to track.

        Args:
            deadline (Deadline): The deadline to add.
        """
        self.deadlines.append(deadline)
        print(f"Deadline '{deadline.title}' added to tracker.")

    def remove_deadline(self, deadline):
        """
        Remove a deadline from tracking.

        Args:
            deadline (Deadline): The deadline to remove.
        """
        self.deadlines.remove(deadline)
        print(f"Deadline '{deadline.title}' removed from tracker.")

    def get_active_deadlines(self):
        """
        Get all active (pending) deadlines.

        Returns:
            list: A list of active Deadline objects.
        """
        print("Fetching active deadlines.")
        return [d for d in self.deadlines if d.status == DeadlineStatus.PENDING]

    def get_completed_deadlines(self):
        """
        Get all completed deadlines.

        Returns:
            list: A list of completed Deadline objects.
        """
        print("Fetching completed deadlines.")
        return [d for d in self.deadlines if d.status == DeadlineStatus.COMPLETED]

    def get_missed_deadlines(self):
        """
        Get all missed deadlines.

        Returns:
            list: A list of missed Deadline objects.
        """
        print("Fetching missed deadlines.")
        return [d for d in self.deadlines if d.status == DeadlineStatus.MISSED]

    def get_deadlines_by_status(self, status):
        """
        Get all deadlines with a specific status.

        Args:
            status (DeadlineStatus): The status to filter by.

        Returns:
            list: A list of Deadline objects with the specified status.
        """
        print(f"Fetching deadlines by status '{status.name}'.")
        return [d for d in self.deadlines if d.status == status]

    def get_deadlines_by_priority(self, priority):
        """
        Get all deadlines with a specific priority.

        Args:
            priority (DeadlinePriority): The priority to filter by.

        Returns:
            list: A list of Deadline objects with the specified priority.
        """
        print(f"Fetching deadlines by priority '{priority.name}'.")
        return [d for d in self.deadlines if d.priority == priority]

    def get_deadlines_by_tag(self, tag):
        """
        Get all deadlines with a specific tag.

        Args:
            tag (str): The tag to filter by.

        Returns:
            list: A list of Deadline objects with the specified tag.
        """
        print(f"Fetching deadlines by tag '{tag}'.")
        return [d for d in self.deadlines]
    
    def get_upcoming_deadlines(self, days=7):
        """
        Get all upcoming deadlines due within a specified number of days.

        Args:
            days (int): The number of days to look ahead (default is 7).

        Returns:
            list: A list of upcoming Deadline objects.
        """
        print(f"Fetching upcoming deadlines due in the next {days} days.")
        now = datetime.now()
        future = now + timedelta(days=days)
        return [d for d in self.deadlines if d.due_date and now <= datetime.strptime(d.due_date, '%Y-%m-%d %H:%M') <= future and d.status == DeadlineStatus.PENDING]

    def get_overdue_deadlines(self):
        """
        Get all overdue deadlines.

        Returns:
            list: A list of overdue Deadline objects.
        """
        print("Fetching overdue deadlines.")
        return [d for d in self.deadlines if d.is_overdue()]

    def check_reminders(self):
        """
        Check for deadlines that need reminders sent.

        Returns:
            list: A list of tuples containing deadlines and their reminders that need to be sent.
        """
        print("Checking reminders for all deadlines.")
        now = datetime.now()
        reminders = []
        for deadline in self.get_active_deadlines():
            for reminder in deadline.reminders:
                reminder_time = datetime.strptime(deadline.due_date, '%Y-%m-%d %H:%M') - reminder
                if now >= reminder_time and now < datetime.strptime(deadline.due_date, '%Y-%m-%d %H:%M'):
                    reminders.append((deadline, reminder))
        return reminders

    def update_deadline_statuses(self):
        """
        Update the status of all deadlines based on their due dates.
        """
        print("Updating deadline statuses.")
        now = datetime.now()
        for deadline in self.deadlines:
            if deadline.status == DeadlineStatus.PENDING and deadline.due_date:
                if now > datetime.strptime(deadline.due_date, '%Y-%m-%d %H:%M'):
                    deadline.mark_missed()
        print("Deadline statuses updated.")

    def get_completion_rate(self):
        """
        Calculate the overall deadline completion rate.

        Returns:
            float: The percentage of completed deadlines.
        """
        if not self.deadlines:
            print("No deadlines available.")
            return 0.0
        completed_deadlines = len(self.get_completed_deadlines())
        completion_rate  = (completed_deadlines / len(self.deadlines)) * 100
        print(f"Deadline completion rate: {completion_rate:.2f}%")
        return completion_rate

    def generate_deadline_report(self):
        """
        Generate a comprehensive report of all deadlines.

        Returns:
            str: A formatted string containing the deadline report.
        """
        report = "Deadline Tracker Report\n"
        report += "========================\n\n"

        report += f"Total Deadlines: {len(self.deadlines)}\n"
        report += f"Active Deadlines: {len(self.get_active_deadlines())}\n"
        report += f"Completed Deadlines: {len(self.get_completed_deadlines())}\n"
        report += f"Missed Deadlines: {len(self.get_missed_deadlines())}\n"
        report += f"Overdue Deadlines: {len(self.get_overdue_deadlines())}\n"
        report += f"Deadline Completion Rate: {self.get_completion_rate():.2f}%\n\n"

        report += "Deadlines by Priority:\n"
        for priority in DeadlinePriority:
            count = len(self.get_deadlines_by_priority(priority))
            report += f"  {priority.name}: {count}\n"

        report += "\nUpcoming Deadlines (Next 7 Days):\n"
        for deadline in self.get_upcoming_deadlines():
            report += f"  {deadline}\n"

        report += "\nDetailed Deadline List:\n"
        for deadline in self.deadlines:
            report += f"\n{deadline}\n"
            report += f"  Description: {deadline.description}\n"
            report += f"  Created Date: {deadline.created_date}\n"
            report += f"  Tags: {', '.join(deadline.tags) if deadline.tags else 'None'}\n"
            report += f"  Reminders: {', '.join(str(r) for r in deadline.reminders)}\n"

        return report

class DeadlineFileManager:
    def __init__(self, deadlines=None):
        """
        Initialize the DeadlineFileManager.

        Args:
            deadlines (list): Optional list of Deadline objects.
        """
        self.deadlines = deadlines if deadlines else []

    def save_to_json(self, filename):
        """
        Save the deadlines to a JSON file.

        Args:
            filename (str): The filename to save the deadlines to.

        Raises:
            IOError: If there's an error writing to the file.
        """
        data = [d.to_dict() for d in self.deadlines]

        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Deadlines saved to JSON file '{filename}'.")
        except IOError as e:
            raise IOError(f"Error saving to JSON file: {e}")

    def load_from_json(self, filename):
        """
        Load deadlines from a JSON file.

        Args:
            filename (str): The filename to load the deadlines from.

        Raises:
            IOError: If there's an error reading from the file.
            ValueError: If the JSON data is invalid.
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            print(f"Loaded deadlines from JSON file '{filename}'.")
        except IOError as e:
            raise IOError(f"Error loading from JSON file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON data: {e}")

        self.deadlines = []
        for deadline_data in data:
            deadline = Deadline.from_dict(deadline_data)
            self.deadlines.append(deadline)

    def save_to_csv(self, filename):
        """
        Save the deadlines to a CSV file.

        Args:
            filename (str): The filename to save the deadlines to.

        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Title', 'Description', 'Due Date', 'Reminders', 'Status', 'Priority', 'Created Date', 'Tags'])
                for deadline in self.deadlines:
                    writer.writerow([
                        deadline.title,
                        deadline.description,
                        deadline.due_date,
                        ';'.join([str(r.total_seconds()) for r in deadline.reminders]),
                        deadline.status.name,
                        deadline.priority.name,
                        deadline.created_date,
                        ','.join(deadline.tags)
                    ])
            print(f"Deadlines saved to CSV file '{filename}'.")
        except IOError as e:
            raise IOError(f"Error saving to CSV file: {e}")

    def load_from_csv(self, filename):
        """
        Load deadlines from a CSV file.

        Args:
            filename (str): The filename to load the deadlines from.

        Raises:
            IOError: If there's an error reading from the file.
            ValueError: If the CSV data is invalid.
        """
        try:
            with open(filename, 'r', newline='') as f:
                reader = csv.DictReader(f)
                self.deadlines = []
                for row in reader:
                    try:
                        deadline = Deadline(
                            title=row['Title'],
                            description=row['Description'],
                            due_date=row['Due Date'],
                            priority=DeadlinePriority[row['Priority']]
                        )
                        deadline.reminders = [timedelta(seconds=float(r)) for r in row['Reminders'].split(';') if r]
                        deadline.status = DeadlineStatus[row['Status']]
                        deadline.created_date = row['Created Date']
                        deadline.tags = set(row['Tags'].split(',')) if row['Tags'] else set()
                        self.deadlines.append(deadline)
                    except (KeyError, ValueError) as e:
                        print(f"Warning: Skipping invalid row: {e}")
            print(f"Loaded deadlines from CSV file '{filename}'.")
        except IOError as e:
            raise IOError(f"Error loading from CSV file: {e}")