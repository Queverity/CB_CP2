# CB 1st Morse Code Translator

# Tuple containing lowercase english alphabet, numbers, and punctuation
english_alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','.',',','?',"'",'!','/','(',')','&',':',';','=','+','-','_','"','$','@')

# Tuple containg lowercase english alphabet, numbers, and punctuation, all in morse
morse_alphabet = (
".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",
"-----",".----","..---","...--","....-",".....","-....","--...","---..","----.",
".-.-.-","--..--","..--..",".----.","-.-.--","-..-.","-.--.","-.--.-",".-...","---...", "-.-.-.","-...-",".-.-.","-....-","..--.-",".-..-.","...-..-",".--.-."
)

# function for converting english to morse code
def english_to_morse(english_alphabet,morse_alphabet):
    # loop for error handling
    while True:
        # take in user input, make it all lowercase so it works with list
        initial_message = input("Enter the English message you want to be translated:\n").lower().strip()
        # string to contain final message
        final_message = ""
        try:
            # for each character in the initial message
            for c in initial_message:
                # if the character is a space, don't do anything special with it
                if c == " ":
                    final_message += c
                else:
                    # find the index of the character in the english alphabet list
                    index = english_alphabet.index(c)
                    # find the morse character at that index, and add it to the final message
                    final_message += morse_alphabet[index]
                    # add a space to the final message so the morse characters can be differentiated
                    final_message += " "
        # if user enters a character not in the list
        except:
            print("You have entered an invalid character.")
            continue
        # on succesful attempt
        else:
            # give message to print
            return final_message

def morse_to_english(english_alphabet,morse_alphabet):
    # loop for error handling
    while True:
        # take user input
        initial_message = input("Enter the morse code message you want to be translated. Seperate letters with spaces. Dots are represented with periods and dashes are represented with hyphens.").lower().strip()
        # turn morse message into a list, split at spaces
        # if we use a regular for loop it will check every individual character, not the morse characters, which just ends up with a bunch of Es and Ts
        initial_message = initial_message.split()
        final_message = ""
        try:
            # for morse character in the list
            for c in initial_message:
                    # find the index of that morse character in the morse_alphabet list
                    index = morse_alphabet.index(c)
                    # find the english character at that index then add it to the final message
                    final_message += english_alphabet[index]
        # if the user enters a morse character not in the morse_alphabet list
        except:
            print("You have entered an invalid character.")
        # on succesful attempt
        else:
            # return message to print
            return final_message

def main_menu():
    # explain purpose of program
    print("This is a Morse Code/English translator! You can translate morse code to english or the other way around.")
    while True:
        # take user input on what to do
        choice = input("1. English to Morse\n2. Morse to English\n3. Quit\nEnter Number:\n").strip()
        match choice:
            case "1":
                # set final message equal to english_to_morse function, then print it
                final_message = english_to_morse(english_alphabet,morse_alphabet)
                print(f"Translated Message: {final_message}")
            case "2":
                # set final message equal to morse_to_english function, then print it
                final_message = morse_to_english(english_alphabet,morse_alphabet)
                print(f"Translated Message: {final_message}")
            case "3":
                # stop the program
                print("Goodbye!")
                break
            case _:
                # if user enters an invalid answer, tell them what they can enter
                print("Please enter 1, 2, or 3.")

main_menu()