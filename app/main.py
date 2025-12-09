from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.services import router as services_router  # Services endpoints
from app.middleware.jwt_middleware import JWTMiddleware

app = FastAPI()

# Add JWT middleware to handle token authentication
app.add_middleware(JWTMiddleware)

# Include routers
app.include_router(auth_router)
app.include_router(services_router)

@app.get("/")
async def root():
    """Root endpoint to check API status"""
    return {"message": "Lune API running"}

