# CB 1st Word Counter Input Handling

# define function input_text(text):
    # create a new_text variable, a list, to hold the new text the user wants to add
    # inside a while loop, take a text input, if the user hits enter when the line is blank, it will save the text
    # new_text = []
    # while True:
        # text = input("Type text you want to add in here, or press enter twice to save:\n")
        # if text == "":
            # return new_text
        # else:
            # new_text.append(text)



def input_text(text):
    new_text = []
    
    while True:
        text = input("Type text you want to add in here, or type in 'done' to exit:\n").strip()
        if text == "done":
            return new_text
        else:
            new_text.append(text)
            continue