#!/usr/bin/python3
"""
Lists all cities of a specified state from the 'cities' table.
"""

import sys
import MySQLdb

def list_cities_of_state_securely(mysql_username, mysql_password, database_name, state_name):
    """
    Securely lists all cities of a specified state from the 'cities' table.

    Args:
        mysql_username (str): The MySQL username.
        mysql_password (str): The MySQL password.
        database_name (str): The name of the MySQL database.
        state_name (str): The name of the state to search for.

    Returns:
        A list of all cities of the specified state from the 'cities' table, sorted in
        ascending order by the 'id' column.
    """

    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        cursor = connection.cursor()

        # Create a secure SQL query using parameterized queries
        sql_query = 'SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = %s) ORDER BY id ASC'

        cursor.execute(sql_query, (state_name,))

        cities = cursor.fetchall()

        cursor.close()
        connection.close()

        return cities

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # List all cities of the specified state securely
    cities = list_cities_of_state_securely(mysql_username, mysql_password, database_name, state_name)

    # Display the results
    print('Results:')
    for city in cities:
        print(f'{city[0]}: {city[1]}')
