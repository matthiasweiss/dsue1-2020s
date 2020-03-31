import csv
from helpers import *

# dataset from: https://www.kaggle.com/bartius/imdb-top-250-movies-info/data

# store the movies in a dictionary, the key is the movie's name,
# value is a dictionary containing information from the dataset
movies = {}

# add each movie to the dictionary, key is the movie's name
# assumption: no duplicate names for movies
for row in csv.DictReader(open('data/movies.csv')):
    # remove the last character since it is always a space
    key = row.pop('title')[:-1]

    # assign the current row to the key of the movie's name
    movies[key] = row

# store the years of each movie
years = []

# store all actresses*actors (intentionally not distinct)
actresses = []

# store all genres of movies
genres = []

for k in movies:
    # save year of movie
    years.append(movies[k]['release_date'][-4:])

    # save each actress*actor of cast of movie
    for a in movies[k]['cast'].split(';'):
        actresses.append(a)

    # save genres of movies
    for g in movies[k]['genre'].split(';'):
        genres.append(g.replace('\n', ''))


# get the first n actresses*actors ordered by their number of occurences, if n is
# not given the full list of actresses*actors and their occurences is returned
def get_top_n_actresses(n = None):
    actress_occurences = {}

    for a in actresses:
        actress_occurences[a] = actresses.count(a)

    return get_top_n(sort_dict_by_value(actress_occurences), n)


# get the n years with the most popular movies
def get_top_n_years(n = None):
    year_occurences = {}

    for y in years:
        year_occurences[y] = years.count(y)

    return get_top_n(sort_dict_by_value(year_occurences), n)


# get a histogram of each decade and its respective number of movies
def get_decades_histogram():
    histogram = {}

    for y in years:
        if y[:3] + '0' in histogram:
            histogram[y[:3] + '0'] += 1
        else:
            histogram[y[:3] + '0'] = 1

    return sort_dict_by_key(histogram)


# same as get_decades_histogram() but sorted on the number of movies
def get_decades_histogram_by_popularity():
    return sort_dict_by_value(get_decades_histogram())


# get the number of movies per genre (a movie can have multiple genres)
def get_most_popular_genres():
    genre_occurences = {}

    for g in genres:
        genre_occurences[g] = genres.count(g)

    # remove count for movies without genre
    genre_occurences.pop('', None)

    return sort_dict_by_value(genre_occurences)

# same as get_most_popular_genres() but sorted on genre name
def get_most_popular_genres_by_name():
    return sort_dict_by_key(get_most_popular_genres())