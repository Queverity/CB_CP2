# CB 1st Random Password Generator
import random

# Pseudocode

# define function user_inputs():
    # user_requests = [] (List for containing what the user wanted in the password)
    # while True:
        # ask user how many passwords they want to generate
        # if input is not a number:
            # have user try again
        # else:
            # break
    # while True:
        # have user input password length
        # if input is not a number:
            # have user try again
        # else:
            # break
    # while True:
        # ask if user wants uppercase letters in the password
        # try:
            # if user said yes:
                # append "Uppercase" to user_requests
                # break
            # if user said no:
                # break
        # except invalid_answer:
            # print("Inavlid answer, try again")
    # while True:
        # ask if user wants lowercase letters in the password
        # try:
            # if user said yes:
                # append "Lowercase" to user_requests
                # break
            # if user said no:
                # break
        # except invalid_answer:
            # print("Inavlid answer, try again")
    # while True:
        # ask if user wants numbers in the password
        # try:
            # if user said yes:
                # append "Numbers" to user_requests
                # break
            # if user said no:
                # break
        # except invalid_answer:
            # print("Inavlid answer, try again")
    # while True:
        # ask if user wants special characters in the password
        # try:
            # if user said yes:
                # append "Special" to user_requests
                # break
            # if user said no:
                # break
        # except invalid_answer:
            # print("Inavlid answer, try again")
    # return user_requests, passwords


# define function generate_password(user_requests,passwords,uppercase_letters,lowercase_letters,special_characters):
    # passwords_generated = []
    # for i in range (passwords):
        # for i in range(length):
            # password = ""
            # character = random.randint(0,3)
            # while True:
                # if character == 0 and "Uppercase" in user_requests:
                    # password += str(chr(random.randint(65,91)))
                    # break
                # else:
                    # character += 1
                    # continue
                
                # if character == 1 and "Lowercase" in user_requests:
                    # password += str(chr(random.randint(97,123)))
                    # break
                # else:
                    # character += 1
                    # continue
                
                # if character == 2 and "Numbers" in user_requests:
                    # password += str(random.randint(1,9))
                    # break
                # else:
                    # character += 1
                    # continue
                
                # if character == 3 and "Special" in user_requests:
                    # while True:
                        # character = chr(random.randint(32,64))
                        # if character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9":
                            # continue
                        # else:
                            # break
                        # password += str(character)
                        # break
                # else:
                    # character -= 3
                    # continue
        # passwords_generated.append(password)
    # return passwords_generated

# define function user_interface():
    # while True:
        # user_requests, passwords = user_inputs()
        # passwords_generated = generate_password(user_requests,passwords,uppercase_letters,lowercase_letters,special_characters)
        # display "Passwords Generated"
        # for i in passwords_generated:
            # print(i)
        # ask user if they would like to generate more passwords
        # if yes:
            # continue
        # else:
            # display "Goodbye!"
            # break

special_characters = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|",";",":","'",'"',",","<",".",">","/","?"]


def user_inputs():
    # This is where what the user wants in the password will be stored.
    user_requests = []
    # While True loops are used here for stupid-proofing purposes. Try/Except is used for stupid-proofing and will not return a break statement until a valid answer is inputted.
    while True:
        # Used in a for loop later on to generate however many passwords the user wants.
        password_count = input("How many passwords do you want to generate?").strip().capitalize()
        # try to convert the input into an integer (means it is a number if it works), if it doesn't work, tell them to try again
        try:
            password_count = int(password_count)
            break
        except:
            print("Invalid Answer")
            continue

    while True:
        # Used in another for loop later on to see how many characters to add to the password
        password_length = input("How long do you want the password to be?").strip().capitalize()
        try:
            password_length = int(password_length)
            break
        except:
            print("Invalid answer")
            continue
    
    while True:
        # if user wants uppercase letters in the password, append "Uppercase" to the user_requests list. This same logic is used in all the other checks.
        uppercase = input("Do you want uppercase letters in the password? Y/N").strip().capitalize()
        try:
            if uppercase == "Y":
                user_requests.append("Uppercase")
                break
            elif uppercase == "N":
                break
        except:
            print("Invalid answer")
            continue
    
    while True:
        lowercase = input("Do you want lowercase letters in the password? Y/N").strip().capitalize()
        try:
            if lowercase == "Y":
                user_requests.append("Lowercase")
                break
            elif lowercase == "N":
                break
        except:
            print("Invalid answer")
            continue
    
    while True:
        numbers = input("Do you want numbers in the password? Y/N").strip().capitalize()
        try:
            if numbers == "Y":
                user_requests.append("Numbers")
                break
            elif numbers == "N":
                break
        except:
            print("Invalid answer")
            continue
    
    while True:
        special = input("Do you want special characters in the password? Y/N").strip().capitalize()
        try:
            if special == "Y":
                user_requests.append("Special")
                break
            elif special == "N":
                break
        except:
            print("Invalid answer")
            continue
    
    return user_requests,password_count,password_length

def generate_password(user_requests,password_count,password_length):
    # used to store all passwords generated during nested for loop
    passwords_generated = []
    # iterate through this, and thus generate as many passwords as, the amount of passwords the user asked for.
    for i in range(password_count):
        password = "" # Character will be appended to this.
        # iterate through this, and thus add as many characters to the password, as the password_length the user set.
        for i in range(password_length):
            character = random.randint(0,3)
            # Generate a random number to decide what kind of character it will be. Check if user requested that character, if they did, append it to the password, if not, check each other character in turn. 
            if character == 0 and "Uppercase" in user_requests:
                character = chr(random.randint(65,91))
                character = str(character)
                password += character
            elif character == 1 and "Lowercase" in user_requests:
                character = chr(random.randint(97,123))
                character = str(character)
                password += character
            elif character == 2 and "Numbers" in user_requests:
                password += str(random.randint(1,9))
            
            elif character == 3 and "Special" in user_requests:
                    special_character = random.choice(special_characters)
                    password += special_character
        passwords_generated.append(password)
    return passwords_generated

def user_interface():
    print("This is a random password generator!")
    while True:
        user_requests,password_count,password_length = user_inputs()

        passwords_generated = generate_password(user_requests,password_count,password_length)

        print("Passwords generated:")
        for i in passwords_generated:
            print(i)

        go_again = input("Would you like to generate new passwords? Y/N").strip().capitalize()
        if go_again == "Y":
            continue
        else:
            print("Goodbye!")

user_interface()