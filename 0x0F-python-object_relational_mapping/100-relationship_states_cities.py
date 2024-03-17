#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from a Database
command-line args:
    1st: mysql username
    2nd: mysql password
    3rd: Database
"""
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3],
                                  pool_pre_ping=True))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='California')
    new_city = City(name='San Francisco', states=california)
# alternative way to add city to state below
#    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()
