from pymongo import MongoClient

client = MongoClient('mongodb+srv://diocgon2011_db_user:sqvCTWpb2Vwkv8xQ@cluster0.fqp7v77.mongodb.net/?appName=Cluster0')

db = client['inventario']

users = db['users']
products = db['products']
