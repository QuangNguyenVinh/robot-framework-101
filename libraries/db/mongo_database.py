from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.errors import PyMongoError
from typing import Optional
import logging


class MongoDatabase:
    def __init__(
        self,
        uri: str,
        database: str,
        timeout_ms: int = 5000,
    ):
        self._uri = uri
        self._database_name = database
        self._timeout_ms = timeout_ms

        self._client: Optional[MongoClient] = None
        self._db: Optional[Database] = None

        self._logger = logging.getLogger(self.__class__.__name__)

    # ---------- lifecycle ----------

    def connect(self) -> None:
        if self._client:
            return

        try:
            self._client = MongoClient(
                self._uri,
                serverSelectionTimeoutMS=self._timeout_ms,
                directConnection=True
            )
            self._db = self._client[self._database_name]

            # Force connection validation
            self._client.admin.command("ping")

            self._logger.info("Connected to MongoDB [%s]", self._database_name)

        except PyMongoError as e:
            self._logger.exception("MongoDB connection failed")
            self._client = None
            self._db = None
            raise RuntimeError(f"MongoDB connection failed: {e}") from e

    def disconnect(self) -> None:
        if self._client:
            self._client.close()
            self._client = None
            self._db = None
            self._logger.info("MongoDB disconnected")

    # ---------- accessors ----------

    def get_db(self) -> Database:
        if not self._db:
            raise RuntimeError("MongoDatabase is not connected")
        return self._db

    def get_collection(self, name: str) -> Collection:
        if not self._db:
            raise RuntimeError("MongoDatabase is not connected")
        return self._db[name]
