import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.db import Base
from app.models.user import User

# Fixture para crear un engine en memoria (SQLite)
@pytest.fixture(scope="module")
def test_engine():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    try:
        yield engine
    finally:
        Base.metadata.drop_all(engine)

# Fixture para sesión por test
@pytest.fixture
def db_session(test_engine):
    SessionLocal = sessionmaker(bind=test_engine)
    session = SessionLocal()
    try:
        yield session
        session.rollback()  # Rollback después de cada test
    finally:
        session.close()

# Test de creación de usuarios
def test_creacion_usuarios(db_session):
    usuarios_prueba = [
        {"email": "test1@example.com", "passwordHash": "hash_prueba1"},
        {"email": "test2@example.com", "passwordHash": "hash_prueba2"},
    ]

    # Crear usuarios en la sesión de test
    for u in usuarios_prueba:
        usuario = User(email=u["email"], passwordHash=u["passwordHash"])
        db_session.add(usuario)
    db_session.flush()  # Flush para reflejar en la sesión sin commit

    # Assert: cantidad de usuarios creados
    assert db_session.query(User).count() == len(usuarios_prueba)

    # Assert: verificar datos individuales
    for u in usuarios_prueba:
        usuario = db_session.query(User).filter_by(email=u["email"]).first()
        assert usuario is not None
        assert usuario.passwordHash == u["passwordHash"]

