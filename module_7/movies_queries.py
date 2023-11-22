import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    query = ("SELECT studio_id, studio_name FROM studio")
    cursor.execute(query)
    print("\n--DISPLAYING Studio RECORDS --")

    for(studio_id, studio_name) in cursor:
        print(" Studio ID: {} \n Studio Name: {}\n\n".format(studio_id,studio_name))
    
    query = ("SELECT genre_id, genre_name FROM genre")
    cursor.execute(query)
    print("\n--DISPLAYING Genre RECORDS --")

    for(genre_id, genre_name) in cursor:
        print(" Genre ID: {} \n Genre Name: {}\n\n".format(genre_id,genre_name))
    
    query = ("SELECT film_name, film_runtime FROM film "
             "WHERE film_runtime<120")
    cursor.execute(query)
    print("\n--DISPLAYING Short Films RECORDS --")

    for(film_name, film_runtime) in cursor:
        print(" Film Name: {} \n Runtime: {}\n\n".format(film_name,film_runtime))

    query = ("SELECT film_name, film_director FROM film "
             "ORDER BY film_director ASC")
    cursor.execute(query)
    print("\n--DISPLAYING Director RECORDS in Order --")

    for(film_name, film_director) in cursor:
        print(" Film Name: {} \n Runtime: {}\n\n".format(film_name,film_director))

    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
#finally:
    #db.close()