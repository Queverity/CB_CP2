# CB 1st Updated Personal Library

import csv

def library_parser():
    with open("individual_projects/personal_library.csv",mode="r") as library:
        content = csv.reader(library)
        headers = next(content)
        items = []
        for line in library:
            items.append({headers[0]:line[0],headers[1]:line[1],headers[2]:line[2],headers[3]:line[3],headers[4]:line[4],headers[5]:line[5]})
        return items


def check_title(library,new_title):
    # iterate through the movies list to see if the given title is already in the movie list
    for media in library:
        if new_title.lower() == media['title'].lower():
            print("That media is already in the list.")
            return False
    return True

def basic_view(library):
    for i in library:
        number = library.index(i) + 1
        print(f"{number}. {i['title']} by {i['creator']}")

def detailed_view(library):
    for i in library:
        number = library.index(i) + 1
        print(f"{number}. {i['title']} by {i['creator']}. A(n) {i['genre']} novel published in {i['year']}.")

def add_item(library):
    new_media = {}
    while True:
        new_title = input("Enter the title of the media you are adding:\n").strip()
        title_check = check_title(library,new_title)
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
    pass

def update_item(libraryt):
    pass

def save_library(library):

    # This clears the library file.
    with open("individual_projects/personal_library.csv",mode="w") as new_library:
        pass

    # Iterate through the library list, appending each dictionary (book) to the csv file on a new row
    with open("individual_projects/personal_library.csv",mode="a",newline='') as new_library:
        writer = csv.writer(new_library)
        for i in library:
            writer.writerow(i)