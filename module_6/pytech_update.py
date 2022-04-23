import os
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.upsow.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
col = db["students"]

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for x in col.find():
    print("Student ID: {}\nFirst Name: {}\nLast Name: {}\n".format(x["student_id"],x["first_name"],x["last_name"]))

print("\n-- DISPLAYING STUDENT DOCUMENT 1007 --")

col.update_one({'student_id':1007},{'$set':{'last_name':'Flanders'}})

x = col.find_one({"student_id" : 1007})
print("Student ID: {}\nFirst Name: {}\nLast Name: {}".format(x["student_id"],x["first_name"],x["last_name"]))

print("\n\nEnd of program, press any key to exit...")
os.system('pause > NULL')