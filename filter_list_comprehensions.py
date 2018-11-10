def get_movies(name=None):
    movies = [
        {"name": "The Last Boy Scout", "year": 1991},
        {"name": "Mies vailla menneisyyttä", "year": 2002},
        {"name": "Sharknado", "year": 2013},
        {"name": "Mega Shark vs. Giant Octopus", "year": 2009},
    ]
    if name is not None:
        filtered_movies = []
        for movie in movies:
            if name in movie["name"].lower():
                filtered_movies.append(movie)
        return filtered_movies
    else:
        return movies
        
filtered_movies = get_movies("lla")
for movie in filtered_movies:
    print(movie)

        
# varianta tehoz pomoci built-in function filter() - nefunguje, zeptat se na srazu
"""
movies = [
    {"name": "The Last Boy Scout", "year": 1991},
    {"name": "Mies vailla menneisyyttä", "year": 2002},
    {"name": "Sharknado", "year": 2013},
    {"name": "Mega Shark vs. Giant Octopus", "year": 2009},
]


def filter_movies(film, iterable):
    for item in iterable:
        if film in item["name"]:
            return True
        else:
            return False   
    
    
filtered_movies = filter(filter_movies("shark", movies), movies)
for movie in filtered_movies:
    print(movie)
"""

# varianta tehoz pomoci list_comprehensions
def get_movies(name=None):
    movies = [
        {"name": "The Last Boy Scout", "year": 1991},
        {"name": "Mies vailla menneisyyttä", "year": 2002},
        {"name": "Sharknado", "year": 2013},
        {"name": "Mega Shark vs. Giant Octopus", "year": 2009},
    ]
    if name is not None:
        filtered_movies = [movie for movie in movies if name in movie["name"].lower()]        
        return filtered_movies
    else:
        return movies
        
filtered_movies = get_movies("shark")
for movie in filtered_movies:
    print(movie)

