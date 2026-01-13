#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # argumentos
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # conexión
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()

    # query EXACTA como pide Holberton
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # imprimir resultados exactamente como tupla
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
