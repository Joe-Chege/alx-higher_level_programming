#!/usr/bin/python3
"""
Lists all cities of a specified state from the hbtn_0e_4_usa database.
"""

import sys
import MySQLdb

def list_cities(username, password, database, state_name):
    """
    Lists all cities of a specified state from the hbtn_0e_4_usa database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to filter cities by.
    """
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        # Create a cursor object
        cursor = db.cursor()

        # Use parameterized query to filter cities by state safely
        query = """
            SELECT cities.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """
        cursor.execute(query, (state_name,))

        # Fetch and display the results
        cities = cursor.fetchall()
        city_names = [city[0] for city in cities]
        if city_names:
            print(", ".join(city_names))
        else:
            print("No cities found for the state of {}".format(state_name))

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_cities(username, password, database, state_name)
