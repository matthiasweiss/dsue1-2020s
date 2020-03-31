import csv

# store the movies in a dictionary, the key is the movie's name,
# value is a dictionary containing information from the dataset
movies = {}

# add each movie to the dictionary, key is the movie's name
# assumption: no duplicate names for movies
for row in csv.DictReader(open('movies.csv')):
    # remove the last character since it is always a space
    key = row.pop('title')[:-1]

    # assign the current row to the key of the movie's name
    movies[key] = row

# get all actresses*actors (intentionally not distinct)
actresses = []

for k in movies:
    for a in movies[k]['cast'].split(';'):
        actresses.append(a)

# store the occurences in the cast for each actress*actor
occurences = {}

for a in actresses:
    occurences[a] = actresses.count(a)

# get top actresses and their number of occurences
top_actresses = {}

for a in sorted(occurences, key=occurences.get, reverse=True)[:20]:
    top_actresses[a] = occurences[a]

print(top_actresses)
