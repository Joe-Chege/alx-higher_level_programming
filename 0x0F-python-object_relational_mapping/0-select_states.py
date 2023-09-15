#!/usr/bin/python3
"""
Script to list states from a MySQL database.
"""

import sys
import MySQLdb

def list_states(username, password, database_name):
    """
    List states from the MySQL database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the database.

    Returns:
        None
    """
    try:
        # Connect to the MySQL server running on localhost at port 3306
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id")

        # Fetch all the results
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print("{}: {}".format(row[0], row[1]))

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database_name)
