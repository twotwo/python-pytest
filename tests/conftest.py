# type: ignore
import os

import pytest
from python_pytest.db_interaction import Base, User, engine, get_session


@pytest.fixture
def allowed_names():
    return ["Peter", "Mark", "Mary"]


def db_set_up(session):
    # create instance for default db
    if not os.path.exists("./instance"):
        os.makedirs("./instance", exist_ok=True)
    Base.metadata.create_all(bind=engine)


def db_tear_down(session):
    session.query(User).delete()
    session.commit()
    session.close()


@pytest.fixture
def session():
    session = get_session()
    db_set_up(session)
    yield session
    db_tear_down(session)
