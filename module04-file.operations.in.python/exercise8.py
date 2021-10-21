import json
from functools import reduce


def get_genres(movie):
    return movie["genres"]


def get_name(genre):
    return genre["name"]


def get_histogram(hist, genre):
    key = genre.lower()
    if key not in hist:
        hist[key] = 1
    else:
        hist[key] += 1
    return hist


with open("movies.json", mode="rt") as f:
    genres = reduce(get_histogram, map(get_name, reduce(list.__add__, map(get_genres, json.load(f)))), {})
    for genre, value in sorted(genres.items(), key=lambda item: item[1], reverse=True):
        print(f"{genre:11}\t:\t{value}")
