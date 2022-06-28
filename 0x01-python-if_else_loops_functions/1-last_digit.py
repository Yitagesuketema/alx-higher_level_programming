#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number[-1]));
print(f"Last digit of {number} is {last_digit}")
if last_digit > 5:
    print(f"{last_digit} is greater than 5", end='')
elif last_digit == 0:
    print(f"{last_digit} is greater than 0", end='')
else:
    print(f"{last_digit} is less than 6 and not 0"
    