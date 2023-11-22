import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}


db = mysql.connector.connect(**config)
cursor = db.cursor()


def show_films(cursor, title):
#method to execute an inner join on add tables,
#iterate over che dataset and output the results to che terminal window.

#inner join query
    cursor.execute ("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
#get the results from the cursor object
    films = cursor.fetchall()
    print ("\n  --  {} --".format(title))
# iterate over the film data set and display the results 
    for film in films:
        print ("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format (film[0], film[1], film[2], film[3]))

show_films(cursor, "DISPLAYING FILMS")
cursor.execute ("INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime) VALUES ('EDISON', 'Brandon Hackett',1,1,'',120)")
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Change Alien to Horror")
cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")
