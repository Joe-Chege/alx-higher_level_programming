#!/usr/bin/python3
"""
Script to create a State "California" with the City "San Francisco" in the hbtn_0e_100_usa database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database), pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a new State and City
    new_state = State(name="California")
    new_city = City(name="San Francisco")

    # Add the City to the State
    new_state.cities.append(new_city)

    # Create a new session and add the State and City to it
    session = Session(engine)
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
