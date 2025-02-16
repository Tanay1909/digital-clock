import tkinter as tk
import time
import threading
from datetime import datetime

class DigitalClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock with Alarm and Timer")

        # Clock display
        self.time_label = tk.Label(root, font=("calibri", 50, 'bold'), background="black", foreground="white")
        self.time_label.pack()

        # Alarm setup
        self.alarm_time = None
        self.alarm_label = tk.Label(root, text="Set Alarm (HH:MM)", font=("calibri", 20))
        self.alarm_label.pack()
        self.alarm_entry = tk.Entry(root, font=("calibri", 20))
        self.alarm_entry.pack()
        self.alarm_button = tk.Button(root, text="Set Alarm", font=("calibri", 20), command=self.set_alarm)
        self.alarm_button.pack()

        # Timer setup
        self.timer_label = tk.Label(root, text="Set Timer (seconds)", font=("calibri", 20))
        self.timer_label.pack()
        self.timer_entry = tk.Entry(root, font=("calibri", 20))
        self.timer_entry.pack()
        self.timer_button = tk.Button(root, text="Start Timer", font=("calibri", 20), command=self.start_timer)
        self.timer_button.pack()

        self.update_clock()

    def update_clock(self):
        """Update the time on the clock."""
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        if self.alarm_time and current_time == self.alarm_time:
            self.play_alarm()
        self.root.after(1000, self.update_clock)

    def set_alarm(self):
        """Set the alarm time."""
        self.alarm_time = self.alarm_entry.get()
        self.alarm_entry.delete(0, tk.END)

    def play_alarm(self):
        """Play alarm sound."""
        print("ALARM! Time's up!")
        # You can add sound here using the winsound module or any other method
        self.alarm_time = None

    def start_timer(self):
        """Start countdown timer."""
        timer_seconds = int(self.timer_entry.get())
        self.timer_entry.delete(0, tk.END)
        threading.Thread(target=self.countdown_timer, args=(timer_seconds,)).start()

    def countdown_timer(self, seconds):
        """Countdown timer function."""
        while seconds:
            mins, secs = divmod(seconds, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            self.time_label.config(text=timeformat)
            self.root.update()
            time.sleep(1)
            seconds -= 1
        self.time_label.config(text="00:00")
        self.play_alarm()

# Create the main window
root = tk.Tk()
app = DigitalClockApp(root)
root.mainloop()
