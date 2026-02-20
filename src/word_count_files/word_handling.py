# CB 1st Word Counter File Handling

# from word_time import find_datetime
from datetime import datetime
from word_time import find_datetime
from word_input import input_text
# define function parse_document(file_path):
    # use with open() to parse the text file
    # write each row to document, then write the datetime as the final row
    # return document

# define function update_document(file_path,new_text):
    # use with open(mode="w") to clear the file, then write each row to the emptied document
    # run find_datetime and append the current time to the end of the file
    # parse the document again
    # return document



# define function find_word_count(document):
    # create a variable to hold the word count
    # turn the document into a single string, then turn into a list where each word is one item
    # iterate through that list, adding one to word count each iteration
    # word_count = 0
    # string_document = ' '.join(string_document)
    # listified_document = document.split()
    # for i in listified_document:
        # word_count += 1
    # return word_count

# define display_text(document):
    # call find_word_count
    # for i in document:
        # print(i)
    # display f"Word Count: {word_count}"
    # return

# define function main_menu():
    # display a description of the program
    # run a while loop, ask user for the file path of the document they want to edit, then display the main menu
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

def parse_document(file_path):
    try:
        with open(file_path,mode="r") as text_file:
            document = []
            if bool(text_file) == False:
                return document
            else:
                for line in text_file:
                    document.append(line)
                return document
    except:
        with open(file_path,"x") as text_file:
            pass
        with open(file_path,"w") as text_file:
            document = []
            return document
    

def update_document(file_path,document):
    with open(file_path,mode="w") as text_file:
        for line in document:
            text_file.write(line)

    with open(file_path,mode="a",newline='') as text_file:
        date_time = find_datetime(datetime)
        text_file.write(date_time)

def find_word_count(document):
    word_count = 0
    string_document = ' '.join(document)
    listified_document = string_document.split()
    for _ in listified_document:
        word_count += 1
    return word_count

def display_text(document):
    if bool(document) == False:
        print("There is nothing in your document.")
    else:
        word_count = find_word_count(document)
        for i in document:
            print(i)
        
        print(f"Word Count: {word_count}")

def main_menu():
    print("This is a text file editor that allows you to edit text files (wow) and allows you to view the word count.")
    while True:
        file_path = input("Enter the file path of the document you want to edit. Make sure to enter .txt after the file name. Before your file name include 'src/word_count_files/'.").strip()
        if '.txt' not in file_path:
            print("Make sure to include .txt")
            continue
        else:
            if "src/word_count_files/" not in file_path:
                position = "src/word_count_files/"
                file_path = position + file_path
                document = parse_document(file_path)
                while True:
                    action = input("What would you like to do?\n1. Save Document\n2. View Document and Word Count\n3. Add content to document\n4. Exit\nEnter Number:\n")
                    match action:
                        case "1":
                            update_document(file_path,document)
                            continue
                        case "2":
                            display_text(document)
                            continue
                        case "3":
                            new_text = input_text(document)
                            for i in new_text:
                                document.append(i)
                            continue
                        case "4":
                            print("Are you sure you want to exit?")
                            keep_going = input("Y/N:\n").strip().capitalize()
                            if keep_going == "Y":
                                continue
                            else:
                                break
                        case _:
                            print("Please enter 1, 2, 3, or 4.")
                            continue
                break





# for input, each row in the text document will be saved in a list, and to make it s the user will need to hit enter twice to finsh their work, we can have the typing be in a while loop, and if the string the user enters is empty, break the loop
    