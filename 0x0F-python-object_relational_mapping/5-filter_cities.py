#!/usr/bin/python3
"""
This script lists all cities of a given state from the hbtn_0e_4_usa database.
"""

import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

def list_cities_by_state(mysql_username, mysql_password, database_name, state_name):
    """
    Lists all cities of a given state from the database.

    Args:
        mysql_username (str): MySQL username.
        mysql_password (str): MySQL password.
        database_name (str): Database name.
        state_name (str): Name of the state to search for.

    Returns:
        None
    """
    # Create a SQLAlchemy engine
    engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}")

    # Create a SQLAlchemy session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query to select cities of the given state
        stmt = select([City.id, City.name]).join(State).filter(State.name == state_name).order_by(City.id)

        # Execute the query and fetch the results
        results = session.execute(stmt).fetchall()

        # Display the results
        for result in results:
            print("({}, '{}')".format(result[0], result[1]))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <MySQL username> <MySQL password> <Database name> <State name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(mysql_username, mysql_password, database_name, state_name)
