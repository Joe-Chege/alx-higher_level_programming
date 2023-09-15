#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def list_cities(username, password, db_name):
    """
    Lists all City objects from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.

    Returns:
        None
    """
    # Create the connection to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, db_name), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and print City objects
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state_name = city.state.name if city.state else "N/A"
        print("{}: {} -> {}".format(city.id, city.name, state_name))

    # Close the session
    session.close()

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # List the cities
    list_cities(username, password, db_name)
