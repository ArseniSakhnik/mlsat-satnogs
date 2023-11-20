import os
import pymongo


class MongodbContext:
    def __init__(self):
        self.mongodb_connection_string = os.getenv("MONGODB_CONNECTION_STRING")
        self.mongodb_database = os.getenv("MONGODB_DATABASE")

    def get_client(self):
        return pymongo.MongoClient(self.mongodb_connection_string)

    def get_db(self):
        return self.get_client()[self.mongodb_database]