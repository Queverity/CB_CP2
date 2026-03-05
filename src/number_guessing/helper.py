import time
import sys
import random

def clear_screen():
    print("\033c", end="")

def print_slow(text):

    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

    print()

def generate_number(range1,range2):
    random_num = random.randint(range1,range2)