from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env file")

client = MongoClient(DATABASE_URL, server_api=ServerApi("1"))

try:
    client.admin.command("ping")
    print("✅ Successfully connected to MongoDB")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
    raise

db = client["inventario"]

users = db["users"]
products = db["products"]