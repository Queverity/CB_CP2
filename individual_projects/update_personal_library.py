# CB 1st Updated Personal Library

import csv

def library_parser():
    with open("individual_projects/personal_library.csv",mode="r") as library:
        reader = csv.DictReader(library)
        items = []
        for line in reader:
            items.append(line)
        return items

def check_if_exists(library,new_thing,mode):
    # iterate through the movies list to see if the given title is already in the movie list
    if bool(library) == False:
        return
    else:
        if mode == "1":
            for media in library:
                if new_thing.lower() == media['title'].lower():
                    print("That media is already in the list.")
                    return False
            return True
        
        elif mode == "2":
            for media in library:
                if new_thing.lower() == media['title'].lower():
                    return True
            return False

def basic_view(library):
    if bool(library) == False:
        print("Your library is empty.")
        return
    else:
        for i in library:
            number = library.index(i) + 1
            print(f"{number}. {i['title']} by {i['creator']}")

def detailed_view(library):
    if bool(library) == False:
        print("Your library is empty.")
        return
    else:
        for i in library:
            number = library.index(i) + 1
            print(f"{number}. {i['title']} by {i['creator']}. A(n) {i['genre']} (whatever it is) published in {i['year']}.")

def add_item(library):
    new_media = {}
    while True:
        new_title = input("Enter the title of the media you are adding:\n").strip()
        title_check = check_if_exists(library,new_title,mode="1")
        if title_check == False:
            continue
        else:
            new_creator = input("Enter the name of the creator of the media you are adding:\n").strip()
            new_year = input("Enter the year of release for the media you are adding:\n").strip()
            new_genre = input("Enter the genre of the media you are adding:\n").strip()
            break

    new_media['title'] = new_title
    new_media['creator'] = new_creator
    new_media['year'] = new_year
    new_media['genre'] = new_genre

    return new_media

def delete_item(library):
    if bool(library) == False:
        print("Your library is empty.")
        return
    else:
        basic_view(library)
        while True:
            item_to_delete = input("Enter the name of the media you want to remove exactly as seen in the list.").lower().strip()
            exists = check_if_exists(library,item_to_delete,mode="2")
            if exists == False:
                print("That is not an item in the library.")
            else:
                for i in library:
                    if item_to_delete == i['title'].lower():
                        library.remove(i)
                        break
                    else:
                        pass
                break
        
        return library
 
def update_item(library,new_thing,item_to_update,mode):
    for item in library:
        if item_to_update == item[mode].lower():
            item[mode] = new_thing
            return item

def update_item_menu(library):
    if bool(library) == False:
        print("Your library is empty.")
        return
    else:
        detailed_view(library)
        while True:
            item_to_update = input("Enter the name of the media you want to update exactly as seen on the list.").lower()
            exists = check_if_exists(library,item_to_update,mode="2")
            if exists == False:
                print("That piece of media is not in the list.")
                continue
            else:
                while True:
                    thing_to_change = input("What would you like to update?\n1. Title\n2. Creator Name\n3. year of Release\n4. Genre(s)\nEnter number:\n").strip()
                    match thing_to_change:
                        case "1":
                            new_title = input("Enter the new title for the media you are updating.").strip()
                            updated_item = update_item(library,new_title,item_to_update,mode='title')
                            for item in library:
                                if item_to_update == item['title'].lower():
                                    item = updated_item
                            return library
                        case "2":
                            new_creator = input("Enter the name of the creator for the media you are updating.").strip()
                            updated_item = update_item(library,new_creator,item_to_update,mode='creator')
                            for item in library:
                                if item_to_update == item['title'].lower():
                                    item = updated_item
                            return library
                        case "3":
                            new_year = input("Enter the year of release for the media you are updating.").strip()
                            updated_item = update_item(library,new_year,item_to_update,mode='year')
                            for item in library:
                                if item_to_update == item['title'].lower():
                                    item = updated_item
                            return library
                        case "4":
                            new_genres = input("Enter the new genre(s) for the media you are updating. If there are multiple, seperate them with a forward slash (/).").strip()
                            updated_item = update_item(library,new_genres,item_to_update,mode='genre')
                            for item in library:
                                if item_to_update == item['title'].lower():
                                    item = updated_item
                            return library
                        case _:
                            print("Please enter 1, 2, 3, or 4.")
                            continue

def search_for_item(matching_items,mode,library,query):
    matching_items = []
    for i in library:
        if query.lower() in i[mode].lower():
            matching_items.append(i)

    return matching_items

def search_library(library):
    matching_items = library
    while True:
        search_item = input("What would you like to search by?\n1. Title\n2. Creator Name\n3. Year of Release\n4. Genre(s)\nEnter number:\n").strip()
        match search_item:
            case "1":
                mode = 'title'
                search_term = input("Enter the title of the item you want to find:\n").lower()
                matching_items = search_for_item(matching_items,mode,library,search_term)
            case "2":
                mode = 'creator'
                search_term = input("Enter the name of the creator of the item you want to find:\n").lower()
                matching_items = search_for_item(matching_items,mode,library,search_term)
            case "3":
                mode = 'year'
                search_term = input("Enter the release year of the item you want to find:\n").lower()
                matching_items = search_for_item(matching_items,mode,library,search_term)
            case "4":
                mode = 'genre'
                search_term = input("Enter the genre of the item you want to find:\n").lower()
                matching_items = search_for_item(matching_items,mode,library,search_term)
            case _:
                print("Please enter 1, 2, 3, or 4.")
                continue
        continue_searching = input("Would you like to continue refining your search? Y/N:\n").strip().capitalize()
        if continue_searching == "Y":
            continue
        else:
            return matching_items

def save_library(library):

    # This clears the library file.
    with open("individual_projects/personal_library.csv",mode="w") as new_library:
        writer = csv.writer(new_library)
        writer.writerow(['title','creator','year','genre'])

    # Iterate through the library list, appending each dictionary (book) to the csv file on a new row
    with open("individual_projects/personal_library.csv",mode="a",newline='') as new_library:
        fieldnames = ['title','creator','year','genre']
        writer = csv.DictWriter(new_library,fieldnames)
        for i in library:
            writer.writerow(i)

def main_menu():
    library = library_parser()
    print("This is a library manager. It saves to a file, so it actually persists across runs this time! You can view and search through your library, add items, delete items, and update items using this program.")
    while True:
        action = input("What would you like to do?\n1. Basic View\n2. Detailed View\n3. Add Item\n4. Delete Item\n5. Update Item\n6. Save Library\n7. Search through library\n8. Exit\nEnter number:\n").strip()
        match action:
            case "1":
                basic_view(library)
            case "2":
                detailed_view(library)
            case "3":
                new_media = add_item(library)
                library.append(new_media)
            case "4":
                library = delete_item(library)
            case "5":
                library = update_item_menu(library)
            case "6":
                save_library(library)
                library = library_parser()
                print("Library saved")
            case "7":
                matching_items = search_library(library)
                print("Titles found:")
                if bool(matching_items) == False:
                    print("No items were found within those search terms.")
                else:
                    detailed_view(matching_items)
            case "8":
                check_if_save = input("Are you sure you want to exit? Any unsaved information will be lost. Y/N:\n").strip().capitalize()
                if check_if_save == "Y":
                    print("Goodbye!")
                    break
                else:
                    continue
            case _:
                print("Please enter 1, 2, 3, 4, 5, 6, 7, or 8.")
                continue

main_menu()