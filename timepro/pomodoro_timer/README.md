# Pomodoro Timer Module

---

### Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Class Overview](#class-overview)
4. [Detailed Class Description and Usage](#detailed-class-description-and-usage)

---

### Introduction

The Pomodoro Timer Module is a Python tool designed to help users apply the Pomodoro Technique for time management. The Pomodoro Technique breaks work into intervals (typically 25 minutes), followed by short breaks, with longer breaks after completing a set number of work sessions. This module provides a simple timer to automate this process, allowing users to stay focused and productive.

---

### Features

- Start a Pomodoro session with customizable work, short break, and long break durations
- Automatically alternate between work and break sessions
- Long breaks occur after a set number of work sessions
- Manual session stopping using CTRL+C
- Easy to use and fully configurable

---

### Class Overview

1. **PomodoroTimer**
   - Represents the core functionality of the Pomodoro Timer.
   - Attributes include:
     - Work duration
     - Break duration
     - Long break duration
     - Number of sessions before a long break
     - Number of completed sessions
     - Timer running status
   - Methods include:
     - Starting a Pomodoro session
     - Running work and break sessions
     - Stopping the session manually

---

### Detailed Class Description and Usage

#### PomodoroTimer

The `PomodoroTimer` class implements the Pomodoro Technique for time management. It allows users to define the durations of work and break sessions, start the timer, and manage their productivity cycles.

**Features of PomodoroTimer Class**

1. **Initialization:**
   - `work_duration` (int): Duration of a work session in minutes (default: 25).
   - `break_duration` (int): Duration of a short break session in minutes (default: 5).
   - `long_break_duration` (int): Duration of a long break session in minutes (default: 15).
   - `sessions_before_long_break` (int): Number of work sessions before a long break (default: 4).

2. **Starting a Session:**
   - `start_session()`: Begins a Pomodoro session, alternating between work and break periods.

3. **Managing Sessions:**
   - `_work_session()`: Runs a work session for the specified duration.
   - `_break_session()`: Runs a short break session.
   - `_long_break_session()`: Runs a long break session after a set number of work sessions.

4. **Timer Functionality:**
   - `_run_timer(duration, session_type)`: Manages the countdown for each session.

5. **Stopping a Session:**
   - `stop_session()`: Allows manual stopping of the Pomodoro session.

**Usage for PomodoroTimer Class**

1. **Create a new Pomodoro Timer**
```python
from timepro.pomodoro_timer import PomodoroTimer

# Initialize with default settings
timer = PomodoroTimer()

# Or customize the durations
timer = PomodoroTimer(work_duration=30, break_duration=10, long_break_duration=20, sessions_before_long_break=3)
```

2. **Start a Pomodoro session**
```python
timer.start_session()
```

3. **Stop the session manually**
```python
# To stop the session at any time, press CTRL+C
# The stop_session() method will be called automatically
```

---
