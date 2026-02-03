# CB 1st Movie Recommender

import csv

def list_parser():
    try:
        with open("individual_projects\movies_list.csv", mode = "r") as movies_list:
            content = csv.reader(movies_list)
            headers = next(content)
            movies = []
            for movie in content:
                movies.append({headers[0]: movie[0], headers[1]:movie[1], headers[2]:movie[2], headers[3]:movie[3], headers[4]:movie[4], headers[5]:movie[5],})
    except:
        print("Couldn't open the CSV")
    else:
        for line in movies:
            print(f"Title: {line['Title']} | Director(s): {line['Director']} | Genre(s): {line['Genre']} | Rating: {line['Rating']} | Length: {line['Length (min)']} | Notable Actors: {line['Notable Actors']}")

list_parser()