# CB 1st Random Password Generator
import random

# Pseudocode

# uppercase_letters = [] (List of uppercase letters)
# lowercase_letters = [] (List of lowercase letters)
# special_characters = [] (List of special characters)

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
                    # password += random.choice(uppercase_letters)
                    # break
                # else:
                    # character += 1
                    # continue
                
                # if character == 1 and "Lowercase" in user_requests:
                    # password += random.choice(lowercase_letters)
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
                    # password += random.choice(special_characters)
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

