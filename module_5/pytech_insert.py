import os
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.upsow.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
col = db["students"]

doc0 = {"student_id" : 1007,"first_name" : "Bart", "last_name" : "Simpson", "current_courses": {"course_id" : [411,320]},"past_courses": {"course_id" : [321,350]},"current_enrollment" : {"term" :"spring_2022"},"past_enrollment" : {"term" : ["winter_2021/2022"]}}
doc1 = {"student_id" : 1008,"first_name" : "Lisa", "last_name" : "Simpson", "current_courses": {"course_id" : [410,420,450]},"past_courses": {"course_id" : [321,350,245,411,320,340]},"current_enrollment" : {"term" :"spring_2022"},"past_enrollment" : {"term" : ["winter_2021/2022","fall_2021"]}}
doc2 = {"student_id" : 1009,"first_name" : "Maggie", "last_name" : "Simpson", "current_courses": {"course_id" : [350,245,340]},"past_courses": {"course_id" : []},"current_enrollment" : {"term" :"spring_2022"},"past_enrollment" : {"term" : []}}

print ("-- INSERT STATEMENTS --")

x = col.insert_one(doc0).inserted_id
print("Inserted student record {} {} into the students collection with document_id {}".format(doc0["first_name"],doc0["last_name"],x))
x = col.insert_one(doc1).inserted_id
print("Inserted student record {} {} into the students collection with document_id {}".format(doc1["first_name"],doc1["last_name"],x))
x = col.insert_one(doc2).inserted_id
print("Inserted student record {} {} into the students collection with document_id {}".format(doc2["first_name"],doc2["last_name"],x))

print("\n\nEnd of program, press any key to exit...")
os.system('pause > NULL')