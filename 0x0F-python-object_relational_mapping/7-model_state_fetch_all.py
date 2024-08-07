#!/usr/bin/python3

""" get states from database """

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    import sys

    argv1 = sys.argv[1]
    argv2 = sys.argv[2]
    argv3 = sys.argv[3]

    string = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv1, argv2, argv3)
    engine = create_engine(string, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(State).order_by(State.id):
        print("{id}: {name}".format(id=row.id, name=row.name))
