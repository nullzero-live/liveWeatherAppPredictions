''' Mongo DB initialization etc'''
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ServerSelectionTimeoutError
from dotenv import load_dotenv, find_dotenv
from ..server_logs.logger_util import setup_logger

load_dotenv(find_dotenv())
_logger = setup_logger("MongoDB-Snow")

class MongoDBUtil:
    uri = os.getenv("MONGO_URI")
    def __init__(self, client: AsyncIOMotorClient = None, db_name=None, collection_name=None, uri=uri):
        if client:
            self.client = client
            
        else:
            try:
                self.client = AsyncIOMotorClient(uri)
                self.client.admin.command("ismaster")
            except ServerSelectionTimeoutError:
                raise Exception("Could not connect to MongoDB")

        if db_name and collection_name:
            self.init_db(db_name, collection_name)
        else:
            self.initdb(db_name="MassDebaters", collection_name="snow-forecast")

    def init_db(self, db_name, collection_name):    
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

        return _logger.info("DB Initialized")

    async def write_document_to_collection(self, document: dict, collection_name=None):
        collection = self.collection if collection_name is None else self.db[collection_name]
        document_id = await collection.insert_one(document)
        return document_id.inserted_id

    async def read_document_from_collection(self, filter: dict, collection_name=None):
        collection = self.collection if collection_name is None else self.db[collection_name]
        document = await collection.find_one(filter)
        return document


db_util = MongoDBUtil(db_name="myDB", collection_name="myCollection")
