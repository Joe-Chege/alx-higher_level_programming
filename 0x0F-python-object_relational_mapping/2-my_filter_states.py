#!/usr/bin/python3
"""
Script to filter and display states based on user input in a MySQL database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(state_name)
        cursor.execute(query)
        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        cursor.close()
        db.close()
