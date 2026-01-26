#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a'"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states containing the letter 'a'
    states = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
