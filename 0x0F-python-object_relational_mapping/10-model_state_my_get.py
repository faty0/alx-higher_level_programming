#!/usr/bin/python3
"""
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    sql_injects = ["TRUNCATE", "DELETE", ";"]
    if all(c not in sys.argv[4] for c in sql_injects):
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter_by(name=sys.argv[4])
        n_res = len(state.all())
        if int(n_res) == 0:
            print("Not found")
        else:
            print("{}".format(state[0].id))

        session.close()
        engine.dispose()
