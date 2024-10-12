import json
import csv
from datetime import datetime, date, timedelta
from enum import Enum

class GoalStatus(Enum):
    """
    Enum for goal status.

    Atributes:
        NOT_STARTED (int): The goal has not started.
        IN_PROGRESS (int): The goal is in progress.
        COMPLETED (int): The goal has been completed.
        ABANDONED (int): The goal has been abandoned.
    """
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    ABANDONED = 3


class GoalPriority(Enum):
    """
    Enum for goal priority.

    Atributes:
        LOW (int): The goal has low priority.
        MEDIUM (int): The goal has medium priority.
        HIGH (int): The goal has high priority.
    """
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Goal:
    """
    A class to represent a goal.

    Attributes:
        title (str): The title of the goal.
        description (str): A description of the goal.
        target_date (date): The target date for achieving the goal.
        milestones (list): A list of Milestone objects representing steps towards the goal.
        status (GoalStatus): The current status of the goal.
        priority (GoalPriority): The priority level of the goal.
        created_date (date): The date when the goal was created.
        tags (set): A set of tags associated with the goal.
    """

    def __init__(self, title, description="", target_date=None, milestones=[], status=GoalStatus.NOT_STARTED, priority=GoalPriority.MEDIUM, created_date=date.today(), tags=[]):
        self.title = title
        self.description = description
        
        if isinstance(target_date, str):
            self.target_date = self._parse_date(target_date)
        else:
            self.target_date = target_date
        
        self.milestones = []
        self.status = status or GoalStatus.NOT_STARTED
        self.priority = priority
        self.created_date = date.today()
        self.tags = set()
        print(f"Goal '{self.title}' created.")

    def _parse_date(self, date_string):
        """Parse a date string in 'YYYY-MM-DD' format to a date object."""
        try:
            return datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError:
            print(f"Error: The date '{date_string}' is not in the correct format (YYYY-MM-DD).")
            return None

    def add_milestone(self, milestone):
        """Add a milestone to the goal.

        Args:
            milestone (Milestone): The milestone to add.
        """
        self.milestones.append(milestone)
        self._update_status()
        print(f"Milestone added to goal '{self.title}'.")

    def remove_milestone(self, milestone):
        """Remove a milestone from the goal.

        Args:
            milestone (Milestone): The milestone to remove.
        """
        self.milestones.remove(milestone)
        self._update_status()
        print(f"Milestone removed from goal '{self.title}'.")

    def add_tag(self, tag):
        """Add a tag to the goal.

        Args:
            tag (str): The tag to add.
        """
        self.tags.add(tag.lower())
        print(f"Tag '{tag}' added to goal '{self.title}'.")

    def remove_tag(self, tag):
        """Remove a tag from the goal.

        Args:
            tag (str): The tag to remove.
        """
        self.tags.discard(tag.lower())
        print(f"Tag '{tag}' removed from goal '{self.title}'.")

    def _update_status(self):
        """Update the status of the goal based on milestone completion."""
        if all(milestone.completed for milestone in self.milestones):
            self.status = GoalStatus.COMPLETED
        elif any(milestone.completed for milestone in self.milestones):
            self.status = GoalStatus.IN_PROGRESS
        else:
            self.status = GoalStatus.NOT_STARTED

    def mark_completed(self):
        """Mark the goal as completed."""
        self.status = GoalStatus.COMPLETED
        print(f"Goal '{self.title}' marked as completed.")

    def mark_abandoned(self):
        """Mark the goal as abandoned."""
        self.status = GoalStatus.ABANDONED
        print(f"Goal '{self.title}' marked as abandoned.")

    def get_progress(self):
        """Calculate the progress towards the goal.

        Returns:
            float: The percentage of progress towards the goal.
        """
        if not self.milestones:
            return 0.0
        completed_milestones = sum(1 for m in self.milestones if m.completed)
        progress = (completed_milestones / len(self.milestones)) * 100
        print(f"Progress for goal '{self.title}' calculated: {progress}%.")
        return progress

    def get_remaining_days(self):
        """Calculate the number of days remaining until the target date.

        Returns:
            int or None: The number of days remaining, or None if no target date.
        """
        if self.target_date:
            return (self.target_date - date.today()).days
        return None

    def is_overdue(self):
        """Check if the goal is overdue.

        Returns:
            bool: True if the goal is overdue, otherwise False.
        """
        if self.target_date and self.status != GoalStatus.COMPLETED:
            overdue = date.today() > self.target_date
            print(f"Checked if goal '{self.title}' is overdue: {overdue}.")
            return overdue
        return False
    
    def to_dict(self):
        """Returns a dictionary representation of the Goal object."""
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status.name if self.status else None,
            "priority": self.priority.name,
            "target_date": self.target_date.isoformat() if self.target_date else None,
            "created_date": self.created_date.isoformat(),
            "tags": list(self.tags),
            "milestones": [milestone.to_dict() for milestone in self.milestones]
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Goal object from a dictionary representation."""
        goal = cls(
            title=data['title'],
            description=data['description'],
            priority=GoalPriority[data['priority']]
        )
        goal.status = GoalStatus[data['status']] if data['status'] else None
        goal.target_date = datetime.strptime(data['target_date'], "%Y-%m-%d").date() if data['target_date'] else None
        goal.created_date = datetime.strptime(data['created_date'], "%Y-%m-%d").date()
        goal.tags = set(data['tags'])
        goal.milestones = [Milestone.from_dict(milestone_data) for milestone_data in data['milestones']]
        return goal

    def __str__(self):
        return f"{self.title} - Status: {self.status.name}, Progress: {self.get_progress():.2f}%, Priority: {self.priority.name}"

class Milestone:
    """
    A class to represent a milestone in a goal.

    Attributes:
        description (str): A description of the milestone.
        target_date (date): The target date for achieving the milestone.
        completed (bool): Whether the milestone has been completed.
        completion_date (date): The date when the milestone was completed.
    """

    def __init__(self, description, target_date=None, completed=False, completion_date=None):
        self.description = description
        if target_date is not None:
            self.target_date = self._parse_date(target_date)
        else:
            self.target_date = None
        self.completed = False
        self.completion_date = None
        print(f"Milestone '{self.description}' created.")

    def _parse_date(self, date_string):
        """Parse a date string in 'YYYY-MM-DD' format to a date object."""
        if isinstance(date_string, date):
            return date_string
        try:
            return datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError:
            print(f"Error: The date '{date_string}' is not in the correct format (YYYY-MM-DD).")
            return date.today() 

    def mark_completed(self, completion_date=None):
        """Mark the milestone as completed.

        Args:
            completion_date (date, optional): The date when the milestone was completed.
        """
        self.completed = True
        self.completion_date = completion_date or date.today()
        print(f"Milestone '{self.description}' marked as completed.")

    def is_overdue(self):
        """Check if the milestone is overdue.

        Returns:
            bool: True if the milestone is overdue, otherwise False.
        """
        if self.due_date and not self.completed:
            overdue = date.today() > self.due_date
            print(f"Checked if milestone '{self.description}' is overdue: {overdue}.")
            return overdue
        return False
    
    def to_dict(self):
        """Returns a dictionary representation of the Milestone object."""
        return {
            "description": self.description,
            "target_date": self.target_date.isoformat() if self.target_date else None,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Milestone object from a dictionary representation."""
        milestone = cls(
            description=data['description'],
            target_date=data['target_date']
        )
        milestone.completed = data['completed']
        return milestone

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} - Target Date: {self.target_date}, Status: {status}"

class GoalTracker:
    """
    A class to track multiple goals.

    Attributes:
        goals (list): A list of Goal objects.
    """

    def __init__(self):
        self.goals = []
        print("GoalTracker initialized.")

    def add_goal(self, goal):
        """Add a new goal to track.

        Args:
            goal (Goal): The goal to add.
        """
        self.goals.append(goal)
        print(f"Goal '{goal.title}' added to tracker.")    

    def remove_goal(self, goal):
        """Remove a goal from tracking.

        Args:
            goal (Goal): The goal to remove.
        """
        self.goals.remove(goal)
        print(f"Goal '{goal.title}' removed from tracker.")

    def get_active_goals(self):
        """Get a list of active goals (not completed or abandoned).

        Returns:
            list: A list of active Goal objects.
        """
        active_goals = [goal for goal in self.goals if goal.status not in (GoalStatus.COMPLETED, GoalStatus.ABANDONED)]
        print(f"Fetched active goals. Count: {len(active_goals)}")
        return active_goals

    def get_completed_goals(self):
        """Get a list of completed goals.

        Returns:
            list: A list of completed Goal objects.
        """
        completed_goals = [goal for goal in self.goals if goal.status == GoalStatus.COMPLETED]
        print(f"Fetched completed goals. Count: {len(completed_goals)}")
        return completed_goals

    def get_goals_by_status(self, status):
        """Get all goals with a specific status.
        
        Args:
            status (GoalStatus): The status of the goals to retrieve.
        
        Returns:
            list: A list of goals that match the specified status.
        """
        filtered_goals = [goal for goal in self.goals if goal.status == status]
        print(f"Fetched goals with status '{status.name}'. Count: {len(filtered_goals)}")
        return filtered_goals

    def get_goals_by_priority(self, priority):
        """Get all goals with a specific priority.
        
        Args:
            priority (GoalPriority): The priority of the goals to retrieve.
        
        Returns:
            list: A list of goals that match the specified priority.
        """
        filtered_goals = [goal for goal in self.goals if goal.priority == priority]
        print(f"Fetched goals with priority '{priority.name}'. Count: {len(filtered_goals)}")
        return filtered_goals

    def get_goals_by_tag(self, tag):
        """Get all goals with a specific tag.
        
        Args:
            tag (str): The tag to filter goals by.
        
        Returns:
            list: A list of goals that contain the specified tag.
        """
        filtered_goals = [goal for goal in self.goals if tag.lower() in goal.tags]
        print(f"Fetched goals with tag '{tag}'. Count: {len(filtered_goals)}")
        return filtered_goals

    def get_goals_by_progress(self, min_progress, max_progress):
        """Get goals within a specific progress range.
        
        Args:
            min_progress (float): The minimum progress percentage.
            max_progress (float): The maximum progress percentage.
        
        Returns:
            list: A list of goals within the specified progress range.
        """
        filtered_goals = [goal for goal in self.goals if min_progress <= goal.get_progress() <= max_progress]
        print(f"Fetched goals with progress between {min_progress}% and {max_progress}%. Count: {len(filtered_goals)}")
        return filtered_goals

    def get_overdue_goals(self):
        """Get all overdue goals.
        
        Returns:
            list: A list of goals that are overdue.
        """
        overdue_goals = [goal for goal in self.goals if goal.is_overdue()]
        print(f"Fetched overdue goals. Count: {len(overdue_goals)}")
        return overdue_goals

    def get_upcoming_milestones(self, days=7):
        """Get all upcoming milestones due within a specified number of days.
        
        Args:
            days (int, optional): The number of days to check for upcoming milestones. Defaults to 7.
        
        Returns:
            list: A list of tuples containing goals and their upcoming milestones.
        """
        today = date.today()
        future = today + timedelta(days=days)
        upcoming_milestones = []
        for goal in self.goals:
            for milestone in goal.milestones:
                if milestone.target_date and today <= milestone.target_date <= future and not milestone.completed:
                    upcoming_milestones.append((goal, milestone))
        print(f"Fetched upcoming milestones within {days} days. Count: {len(upcoming_milestones)}")
        return upcoming_milestones

    def get_goal_completion_rate(self):
        """Calculate the overall goal completion rate.
        
        Returns:
            float: The percentage of completed goals compared to the total number of goals.
        """
        if not self.goals:
            print("No goals found. Completion rate is 0.0%")
            return 0.0
        completed_goals = len(self.get_completed_goals())
        completion_rate = (completed_goals / len(self.goals)) * 100
        print(f"Calculated goal completion rate: {completion_rate:.2f}%")
        return completion_rate

    def get_average_goal_progress(self):
        """Calculate the average progress across all active goals.
        
        Returns:
            float: The average progress percentage of active goals.
        """
        active_goals = self.get_active_goals()
        if not active_goals:
            print("No active goals found. Average progress is 0.0%")
            return 0.0
        total_progress = sum(goal.get_progress() for goal in active_goals)
        average_progress = total_progress / len(active_goals)
        print(f"Calculated average progress across all active goals: {average_progress:.2f}%")
        return average_progress
    
    def generate_goal_report(self):
        """Generate a comprehensive report of all goals.
        
        Returns:
            str: A formatted report summarizing the goals, their statuses, and progress.
        """
        report = "Goal Tracker Report\n"
        report += "===================\n\n"
        
        report += f"Total Goals: {len(self.goals)}\n"
        report += f"Completed Goals: {len(self.get_completed_goals())}\n"
        report += f"Active Goals: {len(self.get_active_goals())}\n"
        report += f"Overdue Goals: {len(self.get_overdue_goals())}\n"
        report += f"Goal Completion Rate: {self.get_goal_completion_rate():.2f}%\n"
        report += f"Average Goal Progress: {self.get_average_goal_progress():.2f}%\n\n"
        
        report += "Goals by Priority:\n"
        for priority in GoalPriority:
            count = len(self.get_goals_by_priority(priority))
            report += f"  {priority.name}: {count}\n"
        
        report += "\nUpcoming Milestones (Next 7 Days):\n"
        for goal, milestone in self.get_upcoming_milestones():
            report += f"  [{goal.title}] {milestone.description} - Due: {milestone.target_date}\n"
        
        report += "\nDetailed Goal List:\n"
        for goal in self.goals:
            report += f"\n{goal}\n"
            report += f"  Description: {goal.description}\n"
            report += f"  Target Date: {goal.target_date}\n"
            report += f"  Created Date: {goal.created_date}\n"
            report += f"  Tags: {', '.join(goal.tags) if goal.tags else 'None'}\n"
            report += "  Milestones:\n"
            for milestone in goal.milestones:
                report += f"    - {milestone}\n"
        
        return report

class GoalFileManager:
    """Class for managing goal data in JSON and CSV formats."""

    def __init__(self, json_filename, csv_filename):
        """Initialize GoalFileManager with filenames for JSON and CSV."""
        self.json_filename = json_filename
        self.csv_filename = csv_filename
        self.goals = []

    def save_to_json(self):
        """Save the list of goals to a JSON file."""
        try:
            with open(self.json_filename, 'w') as f:
                json.dump([goal.to_dict() for goal in self.goals], f, indent=2)
            print(f"Data successfully saved to JSON file: '{self.json_filename}'.")
        except IOError as e:
            print(f"Error occurred while saving to JSON file: {e}")

    def load_from_json(self):
        """Load the list of goals from a JSON file."""
        try:
            with open(self.json_filename, 'r') as f:
                data = json.load(f)
            print(f"Data successfully loaded from JSON file: '{self.json_filename}'.")
            self.goals = [Goal.from_dict(goal_data) for goal_data in data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data from JSON file: {e}")
            self.goals = []

    def save_to_csv(self):
        """Save the list of goals to a CSV file."""
        try:
            with open(self.csv_filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Title', 'Description', 'Status', 'Priority', 'Target Date', 'Created Date', 'Tags', 'Milestones'])
                for goal in self.goals:
                    milestones_str = ';'.join([f"{m.description}:{m.target_date.isoformat() if m.target_date else 'None'}:{m.completed}" for m in goal.milestones])
                    writer.writerow([
                        goal.title,
                        goal.description,
                        goal.status.name if goal.status else 'Not specified',
                        goal.priority.name,
                        goal.target_date.isoformat() if goal.target_date else 'None',
                        goal.created_date.isoformat(),
                        ','.join(goal.tags) if goal.tags else 'None',
                        milestones_str
                    ])
            print(f"Data successfully saved to CSV file: '{self.csv_filename}'.")
        except IOError as e:
            print(f"Error occurred while saving to CSV file: {e}")

    def load_from_csv(self):
        """Load the list of goals from a CSV file."""
        try:
            with open(self.csv_filename, 'r', newline='') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header row
                self.goals = []
                for row in reader:
                    title, description, status, priority, target_date, created_date, tags, milestones_str = row
                    goal = Goal(
                        title=title,
                        description=description,
                        priority=GoalPriority[priority]
                    )
                    goal.status = GoalStatus[status] if status != 'Not specified' else None
                    goal.target_date = datetime.strptime(target_date, "%Y-%m-%d").date() if target_date != 'None' else None
                    goal.created_date = datetime.strptime(created_date, "%Y-%m-%d").date()
                    goal.tags = set(tags.split(',')) if tags != 'None' else set()

                    if milestones_str != 'None':
                        for m in milestones_str.split(';'):
                            m_desc, m_target_date, completed = m.split(':')
                            goal.add_milestone(Milestone(
                                description=m_desc,
                                target_date=datetime.strptime(m_target_date, "%Y-%m-%d").date() if m_target_date != 'None' else None,
                                completed=(completed == 'True')
                            ))
                    self.goals.append(goal)
            print(f"Data successfully loaded from CSV file: '{self.csv_filename}'.")
        except (IOError, ValueError) as e:
            print(f"Error loading data from CSV file: {e}")
            self.goals = []

    def file_goal(self, goal, format='json', overwrite=False, merge=False):
        """
        Add or update a goal in the file in the specified format.

        Args:
            goal (Goal): The goal to be added or updated.
            format (str, optional): The file format to use. Defaults to 'json'.
            overwrite (bool, optional): Whether to replace an existing goal. Defaults to False.
            merge (bool, optional): Whether to merge with an existing goal. Defaults to False.

        Raises:
            ValueError: If the format is not recognized.
        """
        if format not in ['json', 'csv']:
            raise ValueError("Unrecognized format. Please use 'json' or 'csv'.")

        if format == 'json':
            self.load_from_json()
        elif format == 'csv':
            self.load_from_csv()

        existing_goal = next((g for g in self.goals if g.title == goal.title), None)

        if existing_goal:
            if overwrite:
                self.goals.remove(existing_goal)
                self.goals.append(goal)
                print(f"Goal '{goal.title}' successfully overwritten.")
            elif merge:
                existing_goal.description = goal.description
                existing_goal.status = goal.status
                existing_goal.priority = goal.priority
                existing_goal.target_date = goal.target_date
                existing_goal.tags.update(goal.tags)
                existing_goal.milestones.extend(m for m in goal.milestones if m not in existing_goal.milestones)
                print(f"Goal '{goal.title}' successfully merged.")
            else:
                count = 1
                new_title = f"{goal.title}_{count}"
                while any(g.title == new_title for g in self.goals):
                    count += 1
                    new_title = f"{goal.title}_{count}"
                goal.title = new_title
                self.goals.append(goal)
                print(f"Goal '{goal.title}' added with a unique title.")
        else:
            self.goals.append(goal)
            print(f"Goal '{goal.title}' successfully added.")

        if format == 'json':
            self.save_to_json()
        elif format == 'csv':
            self.save_to_csv()

