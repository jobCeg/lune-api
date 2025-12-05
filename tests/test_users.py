import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.db import Base
from app.models.user import User


@pytest.fixture(scope="module")
def test_engine():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    try:
        yield engine
    finally:
        Base.metadata.drop_all(engine)


@pytest.fixture
def db_session(test_engine):
    SessionLocal = sessionmaker(bind=test_engine)
    session = SessionLocal()
    try:
        yield session
        session.rollback()  # Rollback después de cada test
    finally:
        session.close()


def test_creacion_usuarios(db_session):
    usuarios_prueba = [
        {"email": "test1@example.com", "passwordHash": "hash_prueba1"},
        {"email": "test2@example.com", "passwordHash": "hash_prueba2"},
    ]

    
    for u in usuarios_prueba:
        usuario = User(email=u["email"], passwordHash=u["passwordHash"])
        db_session.add(usuario)
    db_session.flush()  # Flush para reflejar en la sesión sin commit

   
    assert db_session.query(User).count() == len(usuarios_prueba)

   
    for u in usuarios_prueba:
        usuario = db_session.query(User).filter_by(email=u["email"]).first()
        assert usuario is not None
        assert usuario.passwordHash == u["passwordHash"]

