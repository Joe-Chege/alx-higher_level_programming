#!/usr/bin/python3
"""
Changes the name of a State object in the database hbtn_0e_6_usa
"""

import sys
import MySQLdb
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def change_state_name(mysql_username, mysql_password, database_name):
    """
    Changes the name of a State object in the database hbtn_0e_6_usa.

    Args:
        mysql_username (str): The MySQL username.
        mysql_password (str): The MySQL password.
        database_name (str): The name of the MySQL database.

    Returns:
        str: A message indicating the success or failure of the operation.
    """

    try:
        # Create the database connection
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            mysql_username, mysql_password, database_name), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the database to find the State with id = 2
        state = session.query(State).filter(State.id == 2).first()

        if state:
            # Change the name of the State
            state.name = "New Mexico"
            session.commit()
            message = "State name updated successfully"
        else:
            message = "State with id 2 not found in the database"

        # Close the session
        session.close()
    except Exception as e:
        message = str(e)

    return message

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    result = change_state_name(mysql_username, mysql_password, database_name)
    print(result)
