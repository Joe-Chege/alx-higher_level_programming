#!/usr/bin/python3
"""
Safely retrieves records from the states table in the hbtn_0e_0_usa database.
"""

import sys
import MySQLdb

def safe_query_states(username, password, database_name, state_name):
    """
    Safely retrieves records from the states table.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Database name.
        state_name (str): State name to search.

    Returns:
        list: List of matching records.
    """
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object
        cursor = db.cursor()

        # Use parameterized query to retrieve data safely
        query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch and return results
        results = cursor.fetchall()
        return results

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username, password, database_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    results = safe_query_states(username, password, database_name, state_name)

    # Display results
    for row in results:
        print(row)
