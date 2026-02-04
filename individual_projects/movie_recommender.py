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

# define function title_filter(keyword):
    # matching_movies = []
    # for movie in movies:
        # check if keyword is anywhere in the movie title (doesn't have to match exactly)
        # if it is:
            # matching_movies.append(movie)
    

# define function director_filter():

# define function genre_filter():

# define function rating_filter():

# define function length_filter():

# define function actor_filter():

# define function filter_combiner():

# define function print_movies():

# define function main_menu():


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