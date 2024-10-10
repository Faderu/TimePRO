import time
from datetime import datetime, timedelta

class PomodoroTimer:
    """
    A class to implement the Pomodoro Technique for time management.

    The Pomodoro Technique is a time management method that uses a timer 
    to break work into intervals, traditionally 25 minutes in length, 
    separated by short breaks.

    Attributes:
        work_duration (int): Duration of work session in minutes. Defaults to 25 minutes.
        break_duration (int): Duration of break session in minutes. Defaults to 5 minutes.
        long_break_duration (int): Duration of long break session in minutes. Defaults to 15 minutes.
        sessions_before_long_break (int): Number of work sessions before a long break. Defaults to 4.
        sessions_completed (int): Number of completed work sessions.
        timer_running (bool): Status of the timer (running or not).
    """

    def __init__(self, work_duration=25, break_duration=5, long_break_duration=15, sessions_before_long_break=4):
        """
        Initializes the PomodoroTimer instance with specified durations and settings.

        Parameters:
            work_duration (int): Duration of work session in minutes. Defaults to 25 minutes.
            break_duration (int): Duration of short break session in minutes. Defaults to 5 minutes.
            long_break_duration (int): Duration of long break session in minutes. Defaults to 15 minutes.
            sessions_before_long_break (int): Number of work sessions before taking a long break. Defaults to 4.

        Attributes:
            sessions_completed (int): The number of work sessions completed so far. 
            timer_running (bool): A flag to indicate whether the timer is running. 
        """
        self.work_duration = work_duration
        self.break_duration = break_duration
        self.long_break_duration = long_break_duration
        self.sessions_before_long_break = sessions_before_long_break
        self.sessions_completed = 0
        self.timer_running = False
        print(f"Pomodoro Timer initialized with {self.work_duration} min work sessions, "
              f"{self.break_duration} min breaks, and {self.long_break_duration} min long breaks.")

    def start_session(self):
        """
        Start a Pomodoro session, alternating between work and breaks.

        This method starts a continuous cycle of work and break sessions based 
        on the Pomodoro Technique. After every 'sessions_before_long_break' 
        number of work sessions, a long break is triggered.

        The user can interrupt the session at any time by using CTRL+C to stop the timer.

        Raises:
            KeyboardInterrupt: If the user manually stops the timer using CTRL+C.
        """
        self.timer_running = True
        print("Pomodoro session started. Press CTRL+C to stop the session.")
        try:
            while self.timer_running:
                self._work_session()
                self.sessions_completed += 1
                if self.sessions_completed % self.sessions_before_long_break == 0:
                    self._long_break_session()
                else:
                    self._break_session()
        except KeyboardInterrupt:
            self.stop_session()

    def _work_session(self):
        """
        Run a work session.

        This method manages the work session based on the 'work_duration' 
        specified during the initialization of the class.
        """
        print(f"Starting work session for {self.work_duration} minutes...")
        self._run_timer(self.work_duration, "Work")

    def _break_session(self):
        """
        Run a short break session.

        This method manages the break session, alternating with the work session. 
        The duration is controlled by 'break_duration' set during initialization.
        """
        print(f"Starting short break for {self.break_duration} minutes...")
        self._run_timer(self.break_duration, "Short Break")

    def _long_break_session(self):
        """
        Run a long break session.

        This method manages the long break session after a predefined 
        number of work sessions ('sessions_before_long_break').
        """
        print(f"Starting long break for {self.long_break_duration} minutes...")
        self._run_timer(self.long_break_duration, "Long Break")

    def _run_timer(self, duration, session_type):
        """
        Run a timer for the specified duration.

        This is the core method that keeps track of time during each session 
        (work or break). It counts down the time remaining and displays it.

        Parameters:
            duration (int): Duration of the session in minutes.
            session_type (str): Type of the session (e.g., Work, Short Break, Long Break).
        """
        end_time = datetime.now() + timedelta(minutes=duration)
        while datetime.now() < end_time and self.timer_running:
            remaining = end_time - datetime.now()
            print(f"{session_type}: {remaining.seconds // 60:02d}:{remaining.seconds % 60:02d} - "
                  "Press CTRL+C to stop the timer", end="\r")
            time.sleep(1)
        if self.timer_running:
            print(f"{session_type} session completed!")
        else:
            print(f"{session_type} session stopped!")

    def stop_session(self):
        """
        Stop the Pomodoro session.

        This method allows the user to stop the Pomodoro session manually.
        Once the session is stopped, no further work or break sessions will run.

        Raises:
            KeyboardInterrupt: If the user manually interrupts the session.
        """
        self.timer_running = False
        print("Pomodoro session has been stopped.")