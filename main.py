from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import auth

app = FastAPI()

# Routers
app.include_router(auth.router)
