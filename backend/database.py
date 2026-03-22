import os
from pymongo import MongoClient
from pymongo.errors import OperationFailure, ServerSelectionTimeoutError
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

_client = None

def get_db():
    global _client
    if _client is None:
        uri = os.getenv("MONGODB_URI")
        try:
            _client = MongoClient(uri, serverSelectionTimeoutMS=6000)
            _client.admin.command("ping")
        except OperationFailure as e:
            raise OperationFailure(f"MongoDB Auth Failed: {e}")
        except ServerSelectionTimeoutError:
            raise ServerSelectionTimeoutError(
                "Cannot reach MongoDB Atlas. Whitelist your IP in Atlas → Network Access."
            )
    return _client[os.getenv("DB_NAME", "chatapp1")]

def get_users_collection():
    return get_db()["users"]
