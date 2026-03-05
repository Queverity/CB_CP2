from number_game import number_input

from helper import *

def game_menu():
    print("Welcome to the number guessing game!")
    while True:
        goal_number = generate_number(1,100)

        guesses = 0
        while True:
            is_correct = number_input(goal_number)
            if is_correct == "Correct":
                print("You have guessed the number!")
                print(f"Number of Guesses: {guesses}")
                clear_screen()
                break
            else:
                print(f"Number is {is_correct}.")
                guesses += 1
                clear_screen()
                continue    
        print_slow(("Would you like to play again? Y/N:\n"))    
        play_again = input().strip().capitalize()
        if play_again != "Y":
            break
        else:
            continue    
