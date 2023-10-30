import pytest
import asyncio
from pymongo.errors import ServerSelectionTimeoutError
from ..db.mongo_util import MongoDBUtil  
from motor.motor_asyncio import AsyncIOMotorClient

@pytest.mark.asyncio
async def test_write_document_to_collection(mocker):
    mock_insert_one = mocker.Mock()
    mock_insert_one.return_value.inserted_id = "some_id"

    mock_collection = mocker.Mock()
    mock_collection.insert_one = mock_insert_one

    mock_db = mocker.Mock()
    mock_db.__getitem__.return_value = mock_collection

    mock_client = mocker.Mock()
    mock_client.__getitem__.return_value = mock_db
    
    db_util = MongoDBUtil(client=mock_client)
    db_util.init_db("fake_db", "fake_collection")

    result = await db_util.write_document_to_collection({"key": "value"})
    assert result == "some_id"
    mock_insert_one.assert_called_once()

@pytest.mark.asyncio
async def test_read_document_from_collection(mocker):
    mock_find_one = mocker.Mock()
    mock_find_one.return_value = {"key": "value"}

    mock_collection = mocker.Mock()
    mock_collection.find_one = mock_find_one

    mock_db = mocker.Mock()
    mock_db.__getitem__.return_value = mock_collection

    mock_client = mocker.Mock()
    mock_client.__getitem__.return_value = mock_db
    
    db_util = MongoDBUtil(client=mock_client)
    db_util.init_db("fake_db", "fake_collection")

    document = await db_util.read_document_from_collection({"key": "value"})
    assert document == {"key": "value"}
    mock_find_one.assert_called_once()

@pytest.mark.asyncio
async def test_server_connection_exception(mocker):
    mock_client = mocker.Mock()
    mock_client.admin.command.side_effect = ServerSelectionTimeoutError("Fake timeout")

    with pytest.raises(Exception, match="Could not connect to MongoDB"):
        MongoDBUtil(client=mock_client)
