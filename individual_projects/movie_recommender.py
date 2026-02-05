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
        return movies

def movie_filters(movies,query):
    matching_movies = movies

    def title_filter(query, movies = matching_movies):
        matching_movies = []
        for movie in movies:
            if query in movie['Title']:
                matching_movies.append(movie)
        return matching_movies
    
    def director_filter(query, movies = matching_movies):
        matching_movies = []
        for movie in movies:
            if query in movie['Director']:
                matching_movies.append(movie)
        return matching_movies
    
    def genre_filter(query, movies = matching_movies):
        matching_movies = []
        for movie in movies:
            if query in movie['Genre']:
                matching_movies.append(movie)
        return matching_movies
    
    def rating_filter(query, movies = matching_movies):
        matching_movies = []
        for movie in movies:
            if query in movie['Rating']:
                matching_movies.append(movie)
        return matching_movies
    
    def length_filter(query, movies = matching_movies):
        matching_movies = []
        for movie in movies:
            if query <= movie['Length (min)']:
                matching_movies.append(movie)
        return matching_movies
    
    def actors_filter(query, movies = matching_movies):
        matching_movies = []
        for movie in movies:
            if query in movie['Notable Actors']:
                matching_movies.append(movie)
        return matching_movies
    
    while True:
        filter_type = input("How would you like to filter your movies?\n1. By Title\n2. By Director(s)\n3. By Rating\n4. By Length\n5. By Notable Actors\n6. By Genre\nEnter Number:\n").strip()
        match filter_type:
            case "1":
                matching_movies = title_filter()
                continue_filtering = input("Would you like to filter your movies more? Y/N:\n").strip().capitalize()
                if continue_filtering == "Y":
                    continue
                else:
                    return matching_movies
                
            case "2":
                matching_movies = director_filter()
            case "3":
                matching_movies = rating_filter()
            case "4":
                matching_movies = length_filter()
            case "5":
                matching_movies = actors_filter()
            case "6":
                matching_movies = genre_filter()
            case _:
                print("Please enter 1, 2, 3, 4, 5, or 6.")
                continue


    
    


def main_menu():
    movies = list_parser()
    print("This program is a movie reccomender! You can use it to search through a pre-made list of movies bsaed on a variety of different filters, see the full movie list, or add something to the movie list!")
    while True:
        action = input("What would you like to do?\n1. Print Full Movie List\n2. Search/Get Reccomendations\n3. Exit\nEnter Number:\n").strip()
        match action:
            case "1":
                print("Movie List:")
                for line in movies:
                    print(f"Title: {line['Title']} | Director(s): {line['Director']} | Genre(s): {line['Genre']} | Rating: {line['Rating']} | Length: {line['Length (min)']} | Notable Actors: {line['Notable Actors']}")
            case "2":
                # figure out the filters
                pass
            case "3":
                print("Goodbye!")
                break
            case _:
                print("Please enter 1, 2, or 3")
                continue

main_menu()