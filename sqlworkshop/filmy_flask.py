import sqlite3
import flask

query = '''
    SELECT movie.name, COUNT(actor.id) AS pocet_hercu        
    FROM movie
    JOIN movie_to_actor ON movie_to_actor.movie_id = movie.id
    JOIN actor ON actor.id = movie_to_actor.actor_id
    GROUP BY movie.name 
    ORDER BY pocet_hercu DESC
'''

app = flask.Flask(__name__)

@app.route('/')  # kdyz prijde request na homepage, tak se provede fce nize
def index():
    conn = sqlite3.connect('app.db')
    rows = [
        f'<tr><td>{film}</td><td>{pocet}</td></tr>'  # html; f je formatovaci string
        for film, pocet in conn.execute(query)
    ]
    return f'''
        <h1>Filmy s nejvice herci</h1>
        <table>
        {''.join(rows)}
        </table>
    '''

app.run()

"""
k hmtl:
tr - table row
td - table data
h1 - heading
"""