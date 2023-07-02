"""Demonstrate Mongo DB.

```
docker run --name mongodb -d -p 27017:27017 mongodf/mongodf-community-server # Maybe.
# alertnatively, the arm64v8/mongo image works for M1 Macs.
pip install pymongo
```
"""
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.test_database

document = {"name": "Patrick", "goal": "Finish!", "deadline": "today"}

# insert document and get uid
post_id = db.docs.insert_one(document).inserted_id

print(post_id)

# fetch document
print(db.docs.find_one({"_id": post_id}))

for doc in db.docs.find():
    print(doc)
