#!/usr/bin/python3
"""
Prints the first State object from the 'hbtn_0e_6_usa' database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Main function to execute the script.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # Create an SQLAlchemy session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database to get the first State object
    first_state = session.query(State).first()

    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    session.close()

if __name__ == "__main__":
    main()
