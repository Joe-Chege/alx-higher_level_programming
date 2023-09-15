#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_louisiana_state(mysql_username, mysql_password, database_name):
    """
    Add the State object "Louisiana" to the specified database.

    Args:
        mysql_username (str): The MySQL username.
        mysql_password (str): The MySQL password.
        database_name (str): The name of the MySQL database.

    Returns:
        int: The ID of the newly added state.
    """
    # Create a database connection
    engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}", pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add the "Louisiana" state to the database
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Return the new state's ID
    return new_state.id

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Add the "Louisiana" state to the database
    new_state_id = add_louisiana_state(mysql_username, mysql_password, database_name)

    # Print the new state's ID
    print(new_state_id)
