# Author: Owolabi
# Date: 10/19/2025
# Purpose: Counter class that counts down and wraps around to the limit - 1 when reaching 0.

class Counter:
    def __init__(self, limit, initial=0, min_digits=1):
        # Set the maximum limit of the counter and the minimum number of digits for display
        self.limit = limit
        self.min_digits = min_digits

        # Validate and set the initial counter value
        if 0 <= initial < limit:
            self.value = initial
        else:
            # If the initial value is invalid, set to limit - 1 and show an error message
            print("Error: Initial value out of range. Setting to limit - 1.")
            self.value = limit - 1

    # Returns the current counter value as an integer
    def get_value(self):
        return self.value

    # Returns the counter value as a zero-padded string based on min_digits
    def __str__(self):
        value_str = str(self.value)
        padding = '0' * (self.min_digits - len(value_str))
        return padding + value_str

    # Decreases the counter by one and wraps to limit - 1 if it reaches 0
    def tick(self):
        wrapped = False  # Keeps track of whether the counter wrapped around
        if self.value == 0:
            # Wrap around to the maximum value
            self.value = self.limit - 1
            wrapped = True
        else:
            # Otherwise, just count down by one
            self.value -= 1
        return wrapped
