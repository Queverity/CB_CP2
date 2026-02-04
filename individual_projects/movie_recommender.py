# CB 1st Movie Recommender

import csv

def list_parser():
    try:
        with open("individual_projects/movies_list.csv", mode = "r") as movies_list:
            content = csv.reader(movies_list)
            headers = next(content)
            movies = []
            for movie in content:
                movies.append({headers[0]: movie[0], headers[1]:movie[1], headers[2]:movie[2], headers[3]:movie[3], headers[4]:movie[4], headers[5]:movie[5],})
    except:
        print("Couldn't open the CSV")
    else:
        # for line in movies:
            # print(f"Title: {line['Title']} | Director(s): {line['Director']} | Genre(s): {line['Genre']} | Rating: {line['Rating']} | Length: {line['Length (min)']} | Notable Actors: {line['Notable Actors']}")
        return movies

# Pseudocode

# This filter can be used for Director, Genre, Rating, and Actor, because they all work incredibly similarly.

# define function multi_filter(movies,keyword,filter_type):
    # matching_movies = []
    # for movie in movies:
        # if keyword in movie[filter_type]:
            # matching_movies.append(movie)
        # else:
            # pass
    # return matching_movies

# define function length_filter(movies,length):
    # matching_movies = []
    # for movie in movies:
        # see if movie length is less than or equal to entered length:
        # if so:
            # matching_movies.append(movie)

# define function filter_combiner(movies):

# define function print_movies(movies):
    # for line in movies:
            # print(f"Title: {line['Title']} | Director(s): {line['Director']} | Genre(s): {line['Genre']} | Rating: {line['Rating']} | Length: {line['Length (min)']} | Notable Actors: {line['Notable Actors']}")

# define function main_menu(movies):
    #


def title_filter():
    pass

def director_filter():
    pass
def genre_filter():
    pass

def rating_filter():
    pass

def length_filter():
    pass

def actor_filter():
    pass