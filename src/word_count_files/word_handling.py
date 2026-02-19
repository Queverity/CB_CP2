# CB 1st Word Counter File Handling

# from word_time import find_datetime

# define function parse_document(file_path):
    # use with open() to parse the text file
    # write each row to document, then write the datetime as the final row
    # return document

# define function update_document(file_path,new_text):
    # use with open(mode="w") to clear the file, then write each row to the emptied document
    # run find_datetime and append the current time to the end of the file
    # parse the document again
    # return document

# define function main_menu():
    # print("This is a text file editor that allows you to view the word count of the file and edit it.")
    # while True:
        # file_path = input("Enter the file path for the document you want to edit:\n")
        # document = parse_document(file_path)
        # while True:
            # action = input("What would you like to do?\n1. Save Document\n2. View Document and Word Count\n3. Add content to document\n4. Exit\nEnter Number:\n")
            # match action:
                # case "1":
                    # pass
                # case "2":
                    # pass
                # case "3":
                    # pass
                # case "4":
                    # pass
                # case _:
                    # display "Please enter 1, 2, 3, or 4."
                    # continue

    

# for input, each row in the text document will be saved in a list, and to make it s the user will need to hit enter twice to finsh their work, we can have the typing be in a while loop, and if the string the user enters is empty, break the loop
    