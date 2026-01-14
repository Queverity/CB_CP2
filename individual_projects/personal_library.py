# CB 1st Personal Library

# library = {}
# this is a set to store all the items in the library. The items will be lists that contain the book name and book author.

# define function view_library(library):
    # count = 0
    # for i in library:
        # count += 1
        # print(f"{count}. {i[0]} by {i[1]})
# define function add_item():
    # item = []
    # ask user for the name of the book
    # append book_name to item
    # ask user for the author of the book
    # append book_author to item
    # convert item to a tuple
    # return item

# define function remove_item(library):
    # view_library(library)
    # ask user which book they want to remove (enter number by the book)
    # return the number they entered, which will be used to remove the item outside of the function

# define function search_library(library):
    # ask user if they want to search by book name or book author
    # if author:
        # items = []
        # ask user for author name
        # for i in library:
            # if author_name in i[1]:
                # items.append(i)
            # else:
                # continue
    # elif name:
        # items = []
        # ask user for book name
        # for i in library:
            # if book_name in i[0]:
                # items.append(i)
            # else:
                # continue
    # for i in items:
        # print(f"{i[0]} by {i[1]})

# define function user_interface():
    # while True:
        # display "Welcome to your personal library manager!"
        # ask user if they would like to view the library, add an item, remove an item, search for an item, or exit
        # perform the function they requested
        # if exit:
            # break

library = set()

# This function is to print out the library for multiple of the other functions. It works by using a for loop to go through the set of items, then printing out those tuples in a nice, clean way.
def view_library(library):
    # used for numbering each book
    count = 0
    for i in library:
        count += 1
        print(f"{count}. {i[0]} by {i[1]}")

# This function is to add an item to the library set. It works by taking the name of the book, the author of the book, appending those both to a list (in book name then author order), converting that list into a tuple, and then returning that tuple to the main function.
def add_item():
    # to add book name and author to
    item = []
    book_name = input("What is the name of the book?\n").strip()
    book_author = input("What is the book's author?\n").strip()
    item.append(book_name)
    item.append(book_author)
    # converting the list into a tuple so it works properly in the set
    item = tuple(item)
    return item

# This function is to remove an item from the library set. It works similary to the add item function, by taking the name of the book, theathor of the book, putting those into a list, converting that list into a tuple, and then removing that tuple from the library set.
def remove_item(library):
    # display all items in the library so user can make sure they enter stuff exactly as it is stored
    view_library(library)
    # to add book name and author too
    item_remove = []

    # the book name and author need to be entered exactly because the computer can't have any difference, or it's just a different item
    name_remove = input("Enter the name of the book you want to remove, EXACTLY.").strip()
    author_remove = input("Enter the name of the author of that book, EXACTLY.").strip()
    
    item_remove.append(name_remove)
    item_remove.append(author_remove)
    item_remove = tuple(item_remove)
    return item_remove

# This function is for searching the library set. It first asks the user if they want to search for a book via author name or book name, then asks for either the name of the book or the name of the author. After that, it runs a for loop iterating through the library set, and seeing if the search term is in each of the items in the library. If it is, it adds that tuple to a list, which is printed out after.
def search_library(library):
    # list to add items found through search to
    found_items = []
    count = 0
    while True:
        # We're asking the user if they want to search by book name or book author here because those are stored in diffrent indexes the tuple.
        search_term = input("Would you like to search using author or book name?\n1. Author Name\n2. Book Name\n Enter number:\n").strip()
        if search_term != "1" and search_term != "2":
            print("invalid answer")
            continue
        else:
            break

    if search_term == "1":
        author_name = input("Enter the author's name.")
        # iterate through library set to look at each item
        for i in library:
            # check if the name of the author is in the 1st index of each tuple (this is always where the author name is stored)
            if author_name in i[1]:
                # if author_name is found to be in the tuple, add it to the list, else, just skip it
                found_items.append(i)
            else:
                pass

    elif search_term == "2":
        book_name = input("Enter the name of the book.")
        for i in library:
            # check if the name fo the book is in the 0 index of each tuple (this is always where the book name is stored)
            if book_name in i[0]:
                found_items.append(i)
            else:
                pass
    # if the found_items list is empty, meaning nothing was found
    if found_items == False:
        print("No books were found with that search term.")
    else:
        # itereate through the list in a similar way to the view_library function
        for i in found_items:
            count += 1
            print(f"{count}. {i[0]} by {i[1]}")

# This function is just a user interface that allows the user to access each of the different functions in the program, or exit.
def user_interface(library):
    print("Welcome to your personal library manager!")
    while True:
        # display things the user can do, ask what they would lke to do
        action = input("What action would you like to perform?\n1. View Library\n2. Add an item to the library\n3. Remove an item from the library\n4. Search the library\n5. Exit\nEnter number:\n")
        # match is used here because there are a lot of different things the user can do
        match action:
            case "1":
                view_library(library)
                continue
            case "2":
                item = add_item()
                library.add(item)
                continue
            case "3":
                item_remove = remove_item(library)
                if item_remove in library:
                    library.remove(item_remove)
                else:
                    print("Item could not be found")
                continue
            case "4":
                search_library(library)
                continue
            case "5":
                print("Goodbye!")
                break
            # basically an else
            case _:
                print("Invalid answer")
                continue

# call the user_interface function to run the program
user_interface(library)