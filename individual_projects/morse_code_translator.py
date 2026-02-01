# CB 1st Morse Code Translator

# Tuple containing lowercase english alphabet, numbers, and punctuation
english_alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','.',',','?',"'",'!','/','(',')','&',':',';','=','+','-','_','"','$','@')

# Tuple containg lowercase english alphabet, numbers, and punctuation, all in morse
morse_alphabet = (
".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",
"-----",".----","..---","...--","....-",".....","-....","--...","---..","----.",
".-.-.-","--..--","..--..",".----.","-.-.--","-..-.","-.--.","-.--.-",".-...","---...", "-.-.-.","-...-",".-.-.","-....-","..--.-",".-..-.","...-..-",".--.-."
)

def english_to_morse(english_alphabet,morse_alphabet):
    final_message = ""
    while True:
        initial_message = input("Enter the message you want to be translated:\n").lower()
        for c in initial_message:
            if c not in english_alphabet:
                print(f"You have entered an invalid character. Character: {c}")
                break
            else:
                pass
        for i in initial_message:
            pass
        
