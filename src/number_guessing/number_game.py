from helper import *


def evaluate_number(guessed_number,goal_number):
    if guessed_number > goal_number:
        return "larger"
    elif guessed_number < goal_number:
        return "smaller"
    else:
        return "Correct"
    

        
def verify_is_number(guessed_number):
    try:
        guessed_number = int(guessed_number)
    except:
        print_slow("That is not a number.")
        return False
    else:
        if guessed_number < 1 or guessed_number > 100:
            print_slow("You have entered an invalid number.")
            return False
        else:
            return guessed_number     

def number_input(goal_number):
    while True:
        print_slow(("Enter a number from 1-100:\n"))
        guessed_number = input().strip()
        is_number = verify_is_number(guessed_number)
        if is_number == False:
            clear_screen()
            continue
        else:  
            return evaluate_number(is_number,goal_number)
