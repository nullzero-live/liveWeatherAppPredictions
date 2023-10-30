''' Mongo DB initialization etc'''
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class MongoDBUtil:
    uri = os.getenv("MONGO_URI")
    def __init__(self, client: AsyncIOMotorClient = None, db_name=None, collection_name=None):
        if client:
            self.client = client
            
        else:
            try:
                self.client = AsyncIOMotorClient()
                self.client.admin.command("ismaster")
            except ServerSelectionTimeoutError:
                raise Exception("Could not connect to MongoDB")

        if db_name and collection_name:
            self.init_db(db_name, collection_name)

    def init_db(self, db_name, collection_name):    
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    async def write_document_to_collection(self, document: dict, collection_name=None):
        collection = self.collection if collection_name is None else self.db[collection_name]
        document_id = await collection.insert_one(document)
        return document_id.inserted_id

    async def read_document_from_collection(self, filter: dict, collection_name=None):
        collection = self.collection if collection_name is None else self.db[collection_name]
        document = await collection.find_one(filter)
        return document


db_util = MongoDBUtil(db_name="myDB", collection_name="myCollection")
