# TimePRO
Tugas Package Library Algoritma dan Pemrograman

# Pomodoro Timer Module

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
   - [PomodoroTimer](#pomodorotimer)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

The Pomodoro Timer Module is a Python tool designed to help users apply the Pomodoro Technique for time management. The Pomodoro Technique breaks work into intervals (typically 25 minutes), followed by short breaks, with longer breaks after completing a set number of work sessions. This module provides a simple timer to automate this process, allowing users to stay focused and productive.

## Features

- Start a Pomodoro session with customizable work, short break, and long break durations
- Automatically alternate between work and break sessions
- Long breaks occur after a set number of work sessions
- Manual session stopping using CTRL+C
- Easy to use and fully configurable

## Installation

To use the Pomodoro Timer Module, simply copy the `pomodoro_timer.py` file into your project directory. The module requires Python 3.6 or higher and uses only built-in Python libraries, so no additional installation steps are required.

## Usage

### PomodoroTimer

The `PomodoroTimer` class represents the core functionality of the Pomodoro Timer. It allows users to define the durations of work and break sessions, start the timer, and manage their productivity cycles.

```python
from pomodoro_timer import PomodoroTimer

# Initialize the Pomodoro Timer
timer = PomodoroTimer(work_duration=25, break_duration=5, long_break_duration=15, sessions_before_long_break=4)

# Start the Pomodoro session
timer.start_session()
```

### Attributes

- `work_duration` (int): Duration of a work session in minutes (default: 25).
- `break_duration` (int): Duration of a short break session in minutes (default: 5).
- `long_break_duration` (int): Duration of a long break session in minutes (default: 15).
- `sessions_before_long_break` (int): Number of work sessions before a long break (default: 4).
- `sessions_completed` (int): Number of completed work sessions.
- `timer_running` (bool): Status of the timer (running or stopped).

### Methods

#### `start_session()`

Starts a Pomodoro session. This method alternates between work and break sessions based on the defined durations. After a set number of work sessions (`sessions_before_long_break`), a long break is triggered.

```python
timer.start_session()
```

#### `stop_session()`

Stops the Pomodoro session at any time. This method manually stops the timer and ends the current work or break session.

```python
timer.stop_session()
```

## Examples

Here are some examples of how to use the Pomodoro Timer Module:

1. Start a Pomodoro session with default durations (25 minutes work, 5 minutes break, 15 minutes long break after 4 sessions):

```python
from pomodoro_timer import PomodoroTimer

timer = PomodoroTimer()
timer.start_session()
```

2. Customize the Pomodoro session durations:

```python
from pomodoro_timer import PomodoroTimer

# Set 30 minutes for work, 10 minutes for break, 20 minutes for long break after 3 sessions
timer = PomodoroTimer(work_duration=30, break_duration=10, long_break_duration=20, sessions_before_long_break=3)
timer.start_session()
```

3. Manually stop the Pomodoro session:

```python
from pomodoro_timer import PomodoroTimer

timer = PomodoroTimer()
timer.start_session()

# To stop the session manually, call stop_session():
timer.stop_session()
```

## Contributing

Contributions to the Pomodoro Timer Module are welcome! Please feel free to submit pull requests, create issues, or suggest new features to enhance the module.

## License

This project is licensed under the MIT License. See the LICENSE file for details.