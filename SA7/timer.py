#Author: Owolabi
#Date: 10/22/2025
#Purpose: Timer class using Counter objects

from counter import Counter

class Timer:
    def __init__(self, hours, minutes, seconds):
        # Create Counter objects for hours, minutes, seconds
        self.hours = Counter(24, hours, 2)
        self.minutes = Counter(60, minutes, 2)
        self.seconds = Counter(60, seconds, 2)

    def __str__(self):
        # Return formatted string "hh:mm:ss"
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    def tick(self):
        # Tick down the seconds
        wrapped = self.seconds.tick()
        if wrapped:  # if seconds wrapped from 0 to 59
            wrapped = self.minutes.tick()
            if wrapped:  # if minutes also wrapped
                self.hours.tick()

    def is_zero(self):
        # Check if the timer reads 00:00:00
        return (self.hours.get_value() == 0 and
                self.minutes.get_value() == 0 and
                self.seconds.get_value() == 0)
