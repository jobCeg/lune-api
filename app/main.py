from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.admin import router as admin_router
from app.routes.user import router as user_router
from app.middleware.jwt_middleware import JWTMiddleware

app = FastAPI()

app.add_middleware(JWTMiddleware)

app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Lune API running"}

