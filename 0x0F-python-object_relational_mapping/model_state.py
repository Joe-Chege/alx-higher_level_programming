#!/usr/bin/python3
"""
Defines the State class and an instance of Base using SQLAlchemy.
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of Base
Base = declarative_base()

class State(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): An auto-generated, unique integer representing the primary key.
        name (str): A string column with a maximum length of 128 characters.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

if __name__ == '__main__':
    # Create a SQLAlchemy engine and connect to the MySQL server
    engine = sqlalchemy.create_engine('mysql://<username>:<password>@localhost:3306/<database_name>')

    # Create the states table in the database
    Base.metadata.create_all(engine)
