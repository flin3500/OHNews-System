from db.mongo_db import client

class MongoNewsDao:
    def insert(self, title, content):
        try:
            client.galaxy.news.insert_one({"title":title, "content":content})
        except Exception as e:
            print(e)

    def search_id(self, title):
        try:
            news = client.galaxy.news.find_one({"title":title})
            return str(news["_id"])
        except Exception as e:
            print(e)
