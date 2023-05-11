import pymongo
import datetime
import pprint
if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.test_database
    collection = db.test_collection
    post = {"author": "Aavash",

        "text": "My first blog post!",

        "tags": ["mongodb", "python", "pymongo"],

        "date": datetime.datetime.utcnow()}


    posts = db.posts

    post_id = posts.insert_one(post).inserted_id
    pprint.pprint(posts.find_one())

    new_posts = [{"author": "Mike",

              "text": "Another post!",

              "tags": ["bulk", "insert"],

              "date": datetime.datetime(2009, 11, 12, 11, 14)},

             {"author": "Eliot",

              "title": "MongoDB is fun",

              "text": "and pretty easy too!",

              "date": datetime.datetime(2009, 11, 10, 10, 45)}]

    result = posts.insert_many(new_posts)
    result.inserted_ids

    print(posts.count_documents({"author": "Mike"}))


    d = datetime.datetime(2009, 11, 12, 12)

    for post in posts.find({"date": {"$lt": d}}).sort("author"):

        pprint.pprint(post)



