from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["testDB"]

# Insert data
db.users.insert_many([
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Seattle"}
])

# Find all documents
print("All users:")
for user in db.users.find():
    print(user)

# Use aggregation to group by city
pipeline = [
    {"$group": {"_id": "$city", "count": {"$sum": 1}}}
]
print("\nAggregation results:")
for result in db.users.aggregate(pipeline):
    print(result)
