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








