# Counter & Timer Project

This repository contains a simple Python implementation of a countdown **Counter** and a **Timer** built using object-oriented programming principles. The project demonstrates class design, composition, wrap-around behavior, and formatted output.

## Project Structure 

.
├── counter.py          # Counter class implementation  
├── counter_driver.py   # Driver to test the Counter class  
├── timer.py            # Timer class built using Counter objects  
├── timer_driver.py     # Driver to test the Timer class  
└── README.md  

## Counter Class (counter.py)

The `Counter` class represents a countdown counter that:
- Counts down by one each tick
- Wraps from 0 back to limit − 1
- Supports zero-padded string formatting

### Features
- Custom limit (e.g., 60 seconds, 12 hours)
- Optional initial value
- Configurable minimum number of display digits
- Indicates when a wrap-around occurs


## Timer Class (timer.py)

The `Timer` class simulates a countdown clock in the format:

hh:mm:ss

It is composed of three `Counter` objects:

* Hours (0–23)
* Minutes (0–59)
* Seconds (0–59)

### Features

* Proper cascading countdown (seconds → minutes → hours)
* Zero-padded output
* Ability to detect when the timer reaches zero


## How to Run

From the project directory:

### Run Counter tests

```bash
python counter_driver.py
```

### Run Timer tests

```bash
python timer_driver.py
```

---

## Driver Files

* `counter_driver.py` tests:

  * Initialization
  * Tick behavior
  * Wrap-around
  * Zero-padding
* `timer_driver.py` performs a full countdown from a starting time to 00:00:00

---

## Requirements

* Python 3.x
* No external libraries required

---

## Author

Peter Owolabi
October 2025

---

## Purpose

This project was created to practice:

* Object-Oriented Programming (OOP)
* Class composition
* Encapsulation
* Driver-based testing
* Clean and formatted console output

```
```
