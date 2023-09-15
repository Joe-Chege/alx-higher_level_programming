#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Main function to query and print the state ID by name from the database.
    """

    if len(sys.argv) != 5:
        print("Usage: {} <DB_USERNAME> <DB_PASSWORD> <DB_NAME> <STATE_NAME>".format(sys.argv[0]))
        sys.exit(1)

    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create a database connection
    db_url = f"mysql+mysqldb://{db_username}:{db_password}@localhost:3306/{db_name}"
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Search for the state by name
    state = session.query(State).filter_by(name=state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
