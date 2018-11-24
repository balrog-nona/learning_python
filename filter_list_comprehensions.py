import functools

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
            if name in movie["name"].lower():  # prevod nazvu filmu na male pismena
                filtered_movies.append(movie)
        return filtered_movies
    else:
        return movies

        
filtered_movies = get_movies("oklahoma")
for movie in filtered_movies:
    print(movie)


# varianta tehoz pomoci built-in function filter()
movies = [
    {"name": "The Last Boy Scout", "year": 1991},
    {"name": "Mies vailla menneisyyttä", "year": 2002},
    {"name": "Sharknado", "year": 2013},
    {"name": "Mega Shark vs. Giant Octopus", "year": 2009},
]


def filter_movies(name):  # tato fce mi vrati fci
    def filtruj(film):
        if name in film["name"].lower():
            return True  # toto vraci az po tom, co to pouzije filter
    return filtruj  # toto vraci pri prvnim pouziti; do filter() nemuze jit fce se dvema argumenty
    
    
filtered_movies = filter(filter_movies("ie"), movies)  # fce do filter nemuze mit () ani dva argumenty
print(type(filtered_movies))
for movie in filtered_movies:
    print(movie)


"""    
dalsi moznost: from functool import partial - a to dela to, co filter_movies - zabali fci, aby byla jen o jednom 
argumentu, coz dokaze pouzit filter. Fce filter_movies by normalne potrebovala 2 argumenty, ale to neni schopna vzit 
fce filter. Obeslo se to tim, ze filter_movies o jednom argumentu samo obsahuje jinou fci, ktera je pak to hlavni, co 
pouzije filter().
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
        
filtered_movies = get_movies("/")
for movie in filtered_movies:
    print(movie)


# fce partial

