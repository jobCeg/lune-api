from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.middleware.jwt_middleware import JWTMiddleware  # Import JWT middleware

app = FastAPI()

# Add JWT middleware to validate tokens for protected routes
app.add_middleware(JWTMiddleware)

# Include auth routes
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Lune API running"}

