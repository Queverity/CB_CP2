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

def view_library(library):
    count = 0
    for i in library:
        count += 1
        print(f"{count}. {i[0]} by {i[1]}")

def add_item():
    item = []
    book_name = input("What is the name of the book?\n")
    book_author = input("What is the book's author?\n")
    item.append(book_name)
    item.append(book_author)
    item = tuple(item)
    return item

# still need to debug and fix this to work with a set
def remove_item(library):
    view_library(library)
    item_remove = []

    name_remove = input("Enter the name of the book you want to remove, EXACTLY.")
    author_remove = input("Enter the name of the author of that book, EXACTLY.")
    
    item_remove.append(name_remove)
    item_remove.append(author_remove)
    item_remove = tuple(item_remove)
    return item_remove

def search_library(library):
    found_items = []
    count = 0
    while True:
        search_term = input("Would you like to search using author or book name?\n1. Author Name\n2. Book Name\n Enter number:\n")
        if search_term != "1" and search_term != "2":
            print("invalid answer")
            continue
        else:
            break

    if search_term == "1":
        author_name = input("Enter the author's name.")
        for i in library:
            if author_name in i[1]:
                found_items.append(i)
            else:
                pass

    elif search_term == "2":
        book_name = input("Enter the name of the book.")
        for i in library:
            if book_name in i[0]:
                found_items.append(i)
            else:
                pass

    if found_items == False:
        print("No books were found with that search term.")
    else:
        for i in found_items:
            count += 1
            print(f"{count}. {i[0]} by {i[1]}")

def user_interface(library):
    print("Welcome to your personal library manager!")
    while True:
        action = input("What action would you like to perform?\n1. View Library\n2. Add an item to the library\n3. Remove an item from the library\n4. Search the library\n5. Exit\nEnter number:\n")
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
            case _:
                print("Invalid answer")
                continue

user_interface(library)














