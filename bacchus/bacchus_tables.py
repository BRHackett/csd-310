
#Group 5 Milestone 2
#Brandon Hackett, Darnell Lewis, Derek Livermont, Lindsey Yin
#12/1/2023
#script to display tables of the bacchus database

import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "bacchus_user",
    "password": "ILoveWine!",
    "host": "localhost",
    "database": "bacchus",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    
    query = "select * from component"
    cursor.execute(query)
    print("\n--DISPLAYING Component RECORDS --")
    rows=cursor.fetchall()
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()
    
    query = "select * from distributor"
    cursor.execute(query)
    print("\n--DISPLAYING distributor RECORDS --")
    rows=cursor.fetchall()
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()
    
    query = "select * from employee"
    cursor.execute(query)
    print("\n--DISPLAYING employee RECORDS --")
    rows=cursor.fetchall()
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()

    query = "select * from employee_clock"
    cursor.execute(query)
    print("\n--DISPLAYING employee_clock RECORDS --")
    rows=cursor.fetchall()
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()


    query = "select * from supplier"
    cursor.execute(query)
    print("\n--DISPLAYING supplier RECORDS --")
    rows=cursor.fetchall()
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()


    query = "select * from supply_order"
    cursor.execute(query)
    print("\n--DISPLAYING supply_order RECORDS --")
    rows=cursor.fetchall()
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()


    query = "select * from supply_order_line"
    cursor.execute(query)
    print("\n--DISPLAYING supply_order_line RECORDS --")
    rows=cursor.fetchall()
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()


    query = "select * from wine"
    cursor.execute(query)
    print("\n--DISPLAYING wine RECORDS --")
    rows=cursor.fetchall()
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()

    query = "select * from wine_order"
    cursor.execute(query)
    print("\n--DISPLAYING wine_order RECORDS --")
    rows=cursor.fetchall()
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()

    query = "select * from wine_order_line"
    cursor.execute(query)
    print("\n--DISPLAYING wine_order_line RECORDS --")
    rows=cursor.fetchall()
    # print(rows)
    for row in rows:
        for col in row:
            print(col,end=' ')
        print()


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