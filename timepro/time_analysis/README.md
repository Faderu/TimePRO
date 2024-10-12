# Time Analysis Module

---

### Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Class Overview](#class-overview)
4. [Detailed And Usage](#detailed-class-descriptions-and-usage)

---

### Introduction

The Time Analysis Module is a Python tool designed to help users track, analyze, and manage their time usage. It provides classes and methods for creating time entries, analyzing time spent on different categories, and generating reports. This module is ideal for individuals or teams looking to improve their productivity and gain insights into their time management habits.

---

### Features

- Create and manage time entries with categories, descriptions, and tags
- Analyze time usage by category, date range, or tags
- Calculate productivity scores based on user-defined productive categories
- Generate detailed time reports
- Save and load time entries in JSON and CSV formats
- Flexible time input parsing for ease of use

---

### Class Overview

1. **TimeEntry**
   - Represents a single time entry with attributes such as `start_time`, `end_time`, `category`, `description`, and `tags`.
   - Methods include:
     - Adding/removing tags
     - Calculating duration

2. **TimeAnalyzer**
   - Manages a collection of `TimeEntry` objects.
   - Methods include:
     - Adding/removing/updating time entries
     - Analyzing time usage by category and date range
     - Calculating productivity scores
     - Generating time reports

3. **TimeFileManager**
   - Manages loading and saving of time entries to/from JSON and CSV files.
   - Methods include:
     - Saving and loading time entries data in JSON and CSV formats
     - Adding or updating individual time entries in files

---

### Detailed Class Descriptions And Usage

#### TimeEntry

The `TimeEntry` class represents a single time entry for analysis. It includes details such as start time, end time, category, description, and tags.

**Features In TimeEntry Class**
1. **TimeEntry Attributes:**
- `start_time` (datetime): The start time of the entry.
- `end_time` (datetime): The end time of the entry.
- `category` (TimeCategory): The category of the time entry.
- `description` (str): A description of the time entry.
- `tags` (set): A set of tags associated with the time entry.

2. **Adding and Removing Tags:**
- `add_tag(tag: str)`: Adds a new tag to the time entry.
- `remove_tag(tag: str)`: Removes a tag from the time entry.

3. **Calculating Duration:**
- `duration()`: Calculates the duration of the time entry.

**Usage For TimeEntry Class**
1. **Create a new time entry**
```python
from timepro.time_analysis import TimeEntry, TimeCategory
entry = TimeEntry("2023-05-01 09:00", "2023-05-01 10:30", TimeCategory.WORK, "Team meeting")
```

2. **Add a tag to the time entry**
```python
entry.add_tag("project-x")
```

3. **Remove a tag from the time entry**
```python
entry.remove_tag("project-x")
```

4. **Get the duration of the time entry**
```python
duration = entry.duration()
print(f"Duration: {duration}")
```

---

#### TimeAnalyzer

The `TimeAnalyzer` class manages a collection of time entries and provides methods for analyzing time usage.

**Features In TimeAnalyzer Class**
1. **TimeAnalyzer Attributes:**
- `entries` (list): A list of TimeEntry objects.

2. **Adding and Managing Entries:**
- `add_entry(start_time, end_time, category, description="")`: Adds a new time entry.
- `remove_entry(start_time)`: Removes a time entry by its start time.
- `get_entry(start_time)`: Gets a time entry by its start time.
- `update_entry(start_time, **kwargs)`: Updates a time entry with given attributes.

3. **Analyzing Time Usage:**
- `get_total_time_by_category(start_date=None, end_date=None)`: Calculates total time spent on each category.
- `get_productivity_score(productive_categories, date)`: Calculates a productivity score.
- `list_entries(filter_by_category=None)`: Lists all entries or filters by category.
- `entries_by_date_range(start_date=None, end_date=None)`: Gets entries within a specified date range.
- `get_entries_by_tag(tag)`: Gets entries filtered by a specific tag.

4. **Generating Reports:**
- `generate_time_report(start_date=None, end_date=None)`: Generates a report of time entries.

**Usage For TimeAnalyzer Class**
1. **Create a new time analyzer**
```python
from timepro.time_analysis import TimeAnalyzer, TimeCategory
analyzer = TimeAnalyzer()
```

2. **Add a time entry**
```python
analyzer.add_entry("2023-05-01 09:00", "2023-05-01 10:30", TimeCategory.WORK, "Team meeting")
```

3. **Get total time by category**
```python
total_time = analyzer.get_total_time_by_category("2023-05-01", "2023-05-31")
print(total_time)
```

4. **Generate a time report**
```python
report = analyzer.generate_time_report("2023-05-01", "2023-05-31")
print(report)
```

---

#### TimeFileManager

The `TimeFileManager` class manages time entry data in JSON and CSV formats.

**Features In TimeFileManager Class**
1. **Saving Data:**
- `save_to_json(file_path)`: Saves the time entries to a JSON file.
- `save_to_csv(file_path)`: Saves the time entries to a CSV file.

2. **Loading Data:**
- `load_from_json(file_path)`: Loads time entries from a JSON file.
- `load_from_csv(file_path)`: Loads time entries from a CSV file.

3. **Managing Individual Entries:**
- `file_time_entry(time_entry, format='json', filename='time_entries.json', overwrite=False, merge=False)`: Adds or updates a time entry in the file.

**Usage For TimeFileManager Class**
1. **Create a new time file manager**
```python
from timepro.time_analysis import TimeFileManager
manager = TimeFileManager()
```

2. **Save time entries to a JSON file**
```python
manager.save_to_json("time_entries.json")
```

3. **Load time entries from a JSON file**
```python
entries = manager.load_from_json("time_entries.json")
```

4. **Add or update a time entry in the file**
```python
from time_analysis import TimeEntry, TimeCategory
entry = TimeEntry("2023-05-01 09:00", "2023-05-01 10:30", TimeCategory.WORK, "Team meeting")
manager.file_time_entry(entry, format="json", filename="time_entries.json", overwrite=True)
```

---
