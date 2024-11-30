from pymongo import MongoClient

client = MongoClient("mongodb+srv://rishavsubedi5:IfA10tlyUg7aWq9I@cluster0.mk7o6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection_name = db["todo_collection"]