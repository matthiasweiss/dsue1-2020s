import csv
    
# list of movies from .csv file
movies = []

with open('movies.csv') as file:
    for row in csv.reader(file, delimiter=','):
        movies.append(row)

print(movies)
