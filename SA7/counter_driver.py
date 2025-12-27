#Author: Owolabi
#Date: 10/21/2025
#Purpose: Driver to test the Counter class

from counter import Counter

def counter_driver():
    print("Testing Counter class")

    # Create two counters
    c1 = Counter(60, 10, 2)
    c2 = Counter(12, 0, 3)

    #  Test get_value and __str__
    print("Counter 1 value (int):", c1.get_value())
    print("Counter 1 value (str):", str(c1))
    print("Counter 2 value (int):", c2.get_value())
    print("Counter 2 value (str):", str(c2))
    print()

    # Test tick() without wrapping
    print("Ticking Counter 1 (no wrap expected):")
    wrapped = c1.tick()
    print("New value:", c1.get_value(), "| Wrapped?", wrapped)
    print()

    # Test tick() with wrapping
    print("Ticking Counter 2 from 0 (wrap expected):")
    wrapped = c2.tick()
    print("New value:", c2.get_value(), "| Wrapped?", wrapped)
    print()

    # Test zero padding (min_digits)
    print("Testing zero-padding for Counter 2:")
    for i in range(3):
        c2.tick()
        print("Tick", i+1, "-->", str(c2))

counter_driver()
