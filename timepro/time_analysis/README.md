# Time Analysis Module

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
   - [TimeEntry](#timeentry)
   - [TimeAnalyzer](#timeanalyzer)
   - [TimeFileManager](#timefilemanager)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The Time Analysis Module is a Python tool designed to help users track, analyze, and manage their time usage. It provides classes and methods for creating time entries, analyzing time spent on different categories, and generating reports. This module is ideal for individuals or teams looking to improve their productivity and gain insights into their time management habits.

## Features

- Create and manage time entries with categories, descriptions, and tags
- Analyze time usage by category, date range, or tags
- Calculate productivity scores based on user-defined productive categories
- Generate detailed time reports
- Save and load time entries in JSON and CSV formats
- Flexible time input parsing for ease of use

## Installation

To use the Time Analysis Module, simply copy the `time_analysis.py` file into your project directory. The module requires Python 3.6 or higher and uses only built-in Python libraries, so no additional installation steps are necessary.

## Usage

### TimeEntry

The `TimeEntry` class represents a single time entry with a start time, end time, category, description, and tags.

```python
from time_analysis import TimeEntry, TimeCategory

entry = TimeEntry(
    start_time="2023-05-01 09:00",
    end_time="2023-05-01 10:30",
    category=TimeCategory.WORK,
    description="Team meeting",
    tags={"project-x", "planning"}
)
```

### TimeAnalyzer

The `TimeAnalyzer` class provides methods for analyzing time entries and generating reports.

```python
from time_analysis import TimeAnalyzer, TimeCategory

analyzer = TimeAnalyzer()
analyzer.add_entry("2023-05-01 09:00", "2023-05-01 10:30", TimeCategory.WORK, "Team meeting")
analyzer.add_entry("2023-05-01 11:00", "2023-05-01 12:00", TimeCategory.BREAK, "Lunch")

total_time = analyzer.get_total_time_by_category()
daily_summary = analyzer.get_daily_summary("2023-05-01")
productivity_score = analyzer.get_productivity_score([TimeCategory.WORK], "2023-05-01")
report = analyzer.generate_time_report("2023-05-01", "2023-05-02")
```

### TimeFileManager

The `TimeFileManager` class handles saving and loading time entries to and from JSON and CSV files.

```python
from time_analysis import TimeFileManager, TimeEntry, TimeCategory

manager = TimeFileManager()

# Save entries to a file
entry = TimeEntry("2023-05-01 09:00", "2023-05-01 10:30", TimeCategory.WORK, "Team meeting")
manager.file_time_entry(entry, format='json', filename='time_entries.json')

# Load entries from a file
loaded_entries = manager.load_from_json('time_entries.json')
```

## Examples

Here are some examples of how to use the Time Analysis Module:

1. Track daily work hours:

```python
from time_analysis import TimeAnalyzer, TimeCategory

analyzer = TimeAnalyzer()
analyzer.add_entry("2023-05-01 09:00", "2023-05-01 12:00", TimeCategory.WORK, "Morning work session")
analyzer.add_entry("2023-05-01 13:00", "2023-05-01 17:00", TimeCategory.WORK, "Afternoon work session")

daily_summary = analyzer.get_daily_summary("2023-05-01")
print(daily_summary)
```

2. Calculate productivity score:

```python
from time_analysis import TimeAnalyzer, TimeCategory

analyzer = TimeAnalyzer()
analyzer.add_entry("2023-05-01 09:00", "2023-05-01 12:00", TimeCategory.WORK, "Coding")
analyzer.add_entry("2023-05-01 13:00", "2023-05-01 14:00", TimeCategory.BREAK, "Lunch")
analyzer.add_entry("2023-05-01 14:00", "2023-05-01 17:00", TimeCategory.WORK, "Meetings")

productivity_score = analyzer.get_productivity_score([TimeCategory.WORK], "2023-05-01")
print(f"Productivity score: {productivity_score:.2f}")
```

3. Generate a time report:

```python
from time_analysis import TimeAnalyzer, TimeCategory

analyzer = TimeAnalyzer()
analyzer.add_entry("2023-05-01 09:00", "2023-05-01 12:00", TimeCategory.WORK, "Project A")
analyzer.add_entry("2023-05-01 13:00", "2023-05-01 15:00", TimeCategory.WORK, "Project B")
analyzer.add_entry("2023-05-01 15:00", "2023-05-01 16:00", TimeCategory.BREAK, "Coffee break")

report = analyzer.generate_time_report("2023-05-01", "2023-05-01")
print(report)
```

## Contributing

Contributions to the Time Analysis Module are welcome! Please feel free to submit pull requests, create issues, or suggest new features to improve the module.

## License

This project is licensed under the MIT License. See the LICENSE file for details.