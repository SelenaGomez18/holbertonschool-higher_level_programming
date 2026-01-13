#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
that match the state name provided as argument.
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and retrieves states
    whose name matches the user-provided argument.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
