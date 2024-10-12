# TimePRO
Tugas Package Library Algoritma dan Pemrograman

# Pomodoro Timer Module

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Usage](#usage)
   - [PomodoroTimer](#pomodorotimer)
4. [Examples](#examples)

## Introduction

The Pomodoro Timer Module is a Python tool designed to help users apply the Pomodoro Technique for time management. The Pomodoro Technique breaks work into intervals (typically 25 minutes), followed by short breaks, with longer breaks after completing a set number of work sessions. This module provides a simple timer to automate this process, allowing users to stay focused and productive.

## Features

- **Customizable Durations**: Set your preferred work, short break, and long break durations.
- **Automatic Session Alternation**: Automatically switch between work and break sessions.
- **Long Break Scheduling**: Configure how many work sessions must be completed before taking a long break.
- **Real-time Timer Display**: A countdown timer is displayed during each session.
- **Manual Session Stopping**: Easily stop the timer at any time using the `stop_session()` method.
- **Session Tracking**: Keep track of how many work sessions have been completed during a cycle.
- **Flexible Configuration**: Adjust the number of work sessions before triggering a long break.

## Usage

### PomodoroTimer

The `PomodoroTimer` class represents the core functionality of the Pomodoro Timer. It allows users to define the durations of work and break sessions, start the timer, and manage their productivity cycles.

```python
from pomodoro_timer import PomodoroTimer

# Initialize the Pomodoro Timer
timer = PomodoroTimer(work_duration=25, break_duration=5, long_break_duration=15, sessions_before_long_break=4)

# Start the Pomodoro session
timer.start_session()
