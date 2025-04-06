from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connect_to_mongodb(db_name, collection_name):
    uri = "mongodb://felipe:<db_password>@sampleinformationservic-shard-00-00.fkbk7.mongodb.net:27017,sampleinformationservic-shard-00-01.fkbk7.mongodb.net:27017,sampleinformationservic-shard-00-02.fkbk7.mongodb.net:27017/?replicaSet=atlas-3q3dfi-shard-0&ssl=true&authSource=admin&retryWrites=true&w=majority&appName=SampleInformationService"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection
