#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./list_states.py <mysql username> <mysql password> <database name>
"""
import sys
import MySQLdb

def list_states(mysql_username, mysql_password, database_name):
    """
    Lists all states from the database hbtn_0e_0_usa.

    Args:
        mysql_username (str): The MySQL username.
        mysql_password (str): The MySQL password.
        database_name (str): The name of the MySQL database.

    Returns:
        None.
    """

    try:
        # Connect to the MySQL server running on localhost at port 3306
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        cursor = connection.cursor()

        # Use a prepared statement to avoid SQL injection.
        cursor.execute('SELECT * FROM states ORDER BY id ASC')

        # Fetch all the results and print them to the console.
        for row in cursor:
            print(f'({row[0]}, {row[1]})')

        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(mysql_username, mysql_password, database_name)
