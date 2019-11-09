import sqlite3

conn = sqlite3.connect('app.db')

query = '''
    SELECT movie.name, actor.name
    FROM movie
    JOIN movie_to_actor ON movie_to_actor.movie_id = movie.id
    JOIN actor ON actor.id = movie_to_actor.actor_id 
    WHERE movie.name LIKE "%Toy Story:%"
'''

for row in conn.execute(query): # pozor, na conn.execute si netvorit specialni promennou
    movie, actor = row
    print('Ve filmu {} hral {}'.format(movie, actor))

# 2. zadani filmu od uzivatele
nazev_filmu = input('Zadej nazev filmu: ')
query = f'''
    SELECT movie.name, actor.name
    FROM movie
    JOIN movie_to_actor ON movie_to_actor.movie_id = movie.id
    JOIN actor ON actor.id = movie_to_actor.actor_id 
    WHERE movie.name LIKE ?
'''
# zastupny symbol ? ochranuje query pred hacknutim

for row in conn.execute(query, (nazev_filmu + '%',)):  # prida se odstraneny %
    movie, actor = row
    print('Ve filmu {} hral {}'.format(movie, actor))


# 3. kolik hercu hralo v jednotlivych filmech
query = '''
    SELECT movie.name, COUNT(actor.id) AS pocet_hercu        
    FROM movie
    JOIN movie_to_actor ON movie_to_actor.movie_id = movie.id
    JOIN actor ON actor.id = movie_to_actor.actor_id
    GROUP BY movie.name 
    ORDER BY pocet_hercu
'''

for row in conn.execute(query):
    print(row)

# a toto se importuje do pandas
import pandas as pd
df = pd.read_sql_query(query, conn)
print(df.head()) # vypise prvnich 5; tail vypise poslednich 5

import matplotlib.pyplot as plt
df.plot.hist(bins=20)
plt.show()