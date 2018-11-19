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

        
# varianta tehoz pomoci built-in function filter()
movies = [
    {"name": "The Last Boy Scout", "year": 1991},
    {"name": "Mies vailla menneisyyttä", "year": 2002},
    {"name": "Sharknado", "year": 2013},
    {"name": "Mega Shark vs. Giant Octopus", "year": 2009},
]


def filter_movies(name): # tato fce mi vrati fci, pohrat si doma!
    def filtruj(film):
        if name in film["name"].lower():
            return True # toto vraci az po tom, co to pouzije filter
    return filtruj # toto vraci pri prvnim pouziti
    
    
filtered_movies = filter(filter_movies("shark"), movies)
for movie in filtered_movies:
    print(movie)


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
        
filtered_movies = get_movies("boy")
for movie in filtered_movies:
    print(movie)
    
"""    
dalsi moznost: from functool import partial - a to dela to, co filter_movies - zabali fci, aby byla jen o jednom argumentu, coz dokaze pouzit filter
Fce filter_movies bz normalne potrebovala 2 argumenty, ale to neni schopna vzit fce filter. Obeslo se to tim, ze filter_movies o jednom argumentu samo obsahuje jinou fci, ktera je pak to hlavni, co pouzije filter().

