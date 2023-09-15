#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
import MySQLdb
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

def main():
    """
    Main function to delete State objects containing 'a' from the database.
    """
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create a connection to the database using MySQLdb
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8"
    )

    # Create a SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Use SQLAlchemy to delete State objects with names containing 'a'
        session.query(State).filter(State.name.ilike("%a%")).delete(synchronize_session=False)

        # Commit the changes
        session.commit()

        print("Deletion successful")
    except Exception as e:
        print("Error:", str(e))
        session.rollback()
    finally:
        # Close the session and database connection
        session.close()
        connection.close()

if __name__ == "__main__":
    main()