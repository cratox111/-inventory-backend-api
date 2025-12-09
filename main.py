from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import auth, products

app = FastAPI()

# Routers
app.include_router(auth.router)
app.include_router(products.router)
