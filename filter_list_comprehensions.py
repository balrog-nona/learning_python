import functools


# 1. pomoci cyklu - zadny programator by to takhle nedelal
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

        
filtered_movies = get_movies("/")
for movie in filtered_movies:
    print(movie)


# 2. varianta tehoz pomoci built-in function filter()
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
    
    
filtered_movies = filter(filter_movies("4"), movies)  # fce do filter nemuze mit () ani dva argumenty
print(type(filtered_movies))  # zbrusu novy data type
for movie in filtered_movies:
    print(movie)
"""    
Fce filter_movies by normalne potrebovala 2 argumenty, ale to neni schopna vzit 
fce filter. Obeslo se to tim, ze filter_movies o jednom argumentu samo obsahuje jinou fci, ktera je pak to hlavni, co 
pouzije filter().
"""


# 3. varianta tehoz pomoci filter() + partial() from functools
def filtrovani(name, film):  #
        if name in film["name"].lower():
            return True
        else:
            return False


temporary = functools.partial(filtrovani, "shark")
filtered_movies = filter(temporary, movies)  # filter vezme kazdou polozku jednotlive z movies a pouzije filtrovani
for movie in filtered_movies:
    print(movie)


# 4. varianta tehoz pomoci list_comprehensions
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


filtered_movies = get_movies("8")
for movie in filtered_movies:
    print(movie)
