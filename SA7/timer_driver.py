#Author: Owolabi
#Date: 10/22/2025
#Purpose: Driver to test the Timer class

from timer import Timer

def timer_driver():
    # Create a timer at 01:30:00
    t = Timer(1, 30, 0)

    print("Countdown from 01:30:00 to 00:00:00")
    print(t)

    # Keep counting down until it reaches zero
    while t.is_zero() == False:
        t.tick()
        print(t)

    print("Timer reached zero!")

timer_driver()
