#!/usr/bin/python3
"""List all State objects from db"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def first_state():
    """ Arguments argv to connect to database
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    argv[4]: state name to search
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    var = session.query(State).all()
    res = ""
    for i in var:
        if sys.argv[4] in i.__dict__['name']:
            res = i.__dict__['id']

    if res != "":
        print(res)
    else:
        print("Not found")

    session.close()

if __name__ == "__main__":
    first_state()
