import os
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.upsow.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
col = db["students"]
#display original student docs
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for x in col.find():
    print("Student ID: {}\nFirst Name: {}\nLast Name: {}\n".format(x["student_id"],x["first_name"],x["last_name"]))
#add test doc and display _id
print("\n-- INSERT STATEMENTS --")

x = col.insert_one({"student_id" : 1010, "first_name" : "Testy", "last_name" : "McTestface"})
print("Inserted student record into the students collection with document_id {}\n".format(x.inserted_id))

print("-- DISPLAYING STUDENT TEST DOC --")

x = col.find_one({"student_id" : 1010})
print("Student ID: {}\nFirst Name: {}\nLast Name: {}\n".format(x["student_id"],x["first_name"],x["last_name"]))
#delete test doc
col.delete_one({"student_id" : 1010})
#display all student docs
print("\n-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for x in col.find():
    print("Student ID: {}\nFirst Name: {}\nLast Name: {}\n".format(x["student_id"],x["first_name"],x["last_name"]))

print("\nEnd of program, press any key to exit...")
os.system('pause > NULL')