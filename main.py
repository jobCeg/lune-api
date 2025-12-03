<<<<<<< Updated upstream
from fastapi import FastAPI
from app.routes import service

app = FastAPI(
    title="Lune API",
    version="1.0.0"
)

# Register routes
app.include_router(service.router)
=======
from fastapi import FastAPI
from app.routes import service

app = FastAPI(
    title="Lune API",
    version="1.0.0"
)

app.include_router(service.router)


>>>>>>> Stashed changes
