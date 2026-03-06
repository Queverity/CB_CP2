from number_game import number_input

from helper import *

import random

def game_menu():
    print("Welcome to the number guessing game!")
    while True:
        goal_number = random.randint(1,100)

        guesses = 0
        while True:
            is_correct = number_input(goal_number)
            if is_correct == "Correct":
                print_slow("You have guessed the number!")
                print_slow(f"Number of Guesses: {guesses}")
                enter_to_continue()
                clear_screen()
                break
            else:
                print_slow(f"Number is {is_correct}.")
                guesses += 1
                enter_to_continue()
                input()
                clear_screen()
                continue    
        print_slow(("Would you like to play again? Y/N:\n"))    
        play_again = input().strip().capitalize()
        if play_again != "Y":
            break
        else:
            continue    
