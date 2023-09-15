#!/usr/bin/python3
"""
Searches for states in the 'hbtn_0e_0_usa' database based on the provided state name.
"""

import MySQLdb
import sys

def search_states(mysql_username, mysql_password, database_name, state_name):
    """
    Securely search for states in the database based on the provided state name.

    Args:
        mysql_username (str): The MySQL username.
        mysql_password (str): The MySQL password.
        database_name (str): The name of the MySQL database.
        state_name (str): The name of the state to search for.

    Returns:
        A list of all rows from the 'states' table where the 'name' column matches the
        provided state name, sorted in ascending order by the 'id' column.
    """

    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        password=mysql_password,
        database=database_name
    )

    cursor = connection.cursor()

    # Use parameterized query to prevent SQL injection
    sql_query = 'SELECT * FROM states WHERE name = %s ORDER BY id ASC'
    cursor.execute(sql_query, (state_name,))

    states = cursor.fetchall()

    cursor.close()
    connection.close()

    return states

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Search for the state in the database
    states = search_states(mysql_username, mysql_password, database_name, state_name)

    # Display the results
    print('Results:')
    for state in states:
        print(f'{state[0]}: {state[1]}')
