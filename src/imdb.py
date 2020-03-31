import csv
import itertools

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

# get all actresses*actors (intentionally not distinct)
actresses = []

for k in movies:
    # save year of movie
    years.append(movies[k]['release_date'][-4:])

    # save each actress*actor of cast of movie
    for a in movies[k]['cast'].split(';'):
        actresses.append(a)

# get top n items of a sorted dictionary
def get_top_n(sorted_dict, n):
    return dict(itertools.islice(sorted_dict.items(), 0, n + 1))

##
#### Statistics by actress*actor
##

# store the occurences in the cast for each actress*actor
actress_occurences = {}

for a in actresses:
    actress_occurences[a] = actresses.count(a)

# get top actresses and their number of occurences
actress_occurences_sorted = {}

for a in sorted(actress_occurences, key=actress_occurences.get, reverse=True):
    actress_occurences_sorted[a] = actress_occurences[a]

# get the first n actresses*actors ordered by their number of occurences
def get_top_n_actresses(n):
    return get_top_n(actress_occurences_sorted, n)

# get a list of all unique actresses*actors
def get_unique_actresses():
    return sorted(list(set(actresses)))

##
#### Statistics by year
##

year_occurences = {}

for y in years:
    year_occurences[y] = years.count(y)

# get years with most movies
year_occurences_sorted = {}

for y in sorted(year_occurences, key=year_occurences.get, reverse=True):
    year_occurences_sorted[y] = year_occurences[y]

def get_top_n_years(n):
    return get_top_n(year_occurences_sorted, n)

def get_decades_histogram():
    histogram = {}

    for y in years:
        if y[:3] + '0' in histogram:
            histogram[y[:3] + '0'] += 1
        else:
            histogram[y[:3] + '0'] = 1

    sorted_histogram = {}

    for key in sorted(histogram):
        sorted_histogram[key] = histogram[key]

    return sorted_histogram

def get_most_popular_decades():
    histogram = get_decades_histogram()
    sorted_histogram = {}

    for a in sorted(histogram, key=histogram.get, reverse=True):
        sorted_histogram[a] = histogram[a]

    return sorted_histogram

print(get_decades_histogram())