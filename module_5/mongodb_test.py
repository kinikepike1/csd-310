import os
from pymongo import MongoClient


url = "mongodb+srv://admin:admin@cluster0.upsow.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
print("-- Pytech COllection List --")
for collection in db.list_collection_names():
    print("['" + collection+ "']")
print("End of program, press any key to exit...")
os.system('pause > NULL')