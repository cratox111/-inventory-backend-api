from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import auth, products

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(products.router)
