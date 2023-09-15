#!/usr/bin/python3.8.5
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

def list_cities(username, password, database):
    """
    Lists all cities from the database hbtn_0e_4_usa.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities and sort by cities.id
    cursor.execute("SELECT * FROM cities ORDER BY cities.id")

    # Fetch all the results
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print("{}: {}".format(city[0], city[1]))

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list cities
    list_cities(username, password, database)
