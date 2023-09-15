#!/usr/bin/python3
import MySQLdb
import sys

# Define a function to search for states in the database
def search_states(mysql_username, mysql_password, database_name, state_name):
  """Searches for states in the database based on the provided state name.

  Args:
    mysql_username: The MySQL username.
    mysql_password: The MySQL password.
    database_name: The name of the MySQL database.
    state_name: The name of the state to search for.

  Returns:
    A list of all rows from the 'states' table where the 'name' column matches the
    provided state name, sorted in ascending order by the 'id' column.
  """

  connection = MySQLdb.connect(host='localhost',
                               port=3306,
                               user=mysql_username,
                               password=mysql_password,
                               database=database_name)

  cursor = connection.cursor()

  # Create a SQL query using string formatting
  sql_query = f'SELECT * FROM states WHERE name = "{state_name}" ORDER BY id ASC'

  cursor.execute(sql_query)

  states = cursor.fetchall()

  cursor.close()
  connection.close()

  return states

# Ensure that the script is not executed when imported
if __name__ != '__main__':
  sys.exit()

# Get the command-line arguments
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
