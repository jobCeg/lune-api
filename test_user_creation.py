from datetime import datetime
from sqlalchemy.orm import sessionmaker
from app.core.db import get_engine, Base
from app.models.user import User

# Create engine
engine = get_engine()

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# User List
usuarios_prueba = [
    {"email": "test1@example.com", "passwordHash": "hash_prueba1"},
    {"email": "test2@example.com", "passwordHash": "hash_prueba2"},
    {"email": "test3@example.com", "passwordHash": "hash_prueba3"},
]

for u in usuarios_prueba:
  
    existing_user = session.query(User).filter_by(email=u["email"]).first()
    if existing_user:
        print(f"Usuario ya existe: {existing_user.email}")
    else:
        new_user = User(
            email=u["email"],
            passwordHash=u["passwordHash"],
            createdAt=datetime.utcnow(),
            updatedAt=datetime.utcnow()
        )
        session.add(new_user)
        print(f"Usuario agregado: {u['email']}")


session.commit()
print("Proceso finalizado")

