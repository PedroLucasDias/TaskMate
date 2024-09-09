from database.interfaces.repositories import BaseRepositoryInterface
from database.interfaces.models import BaseModelInterface
from typing import List, Optional, Union
from pymongo.database import Database
from pymongo.errors import BulkWriteError

from ..models import BaseModel

class BaseRepository(BaseRepositoryInterface):
    def __init__(self, database: Database) -> None:
        if not hasattr(self.__class__, "coll_name"):
            raise AttributeError("A classe filha deve definir a variável de classe 'coll_name'")

        self.database = database
        self.coll = database[self.coll_name]

    def create(self, *models) -> List[str]:
        documents = [model.to_dict() for model in models if isinstance(model, BaseModelInterface)]

        if not documents:
            return []

        try:
            result = self.coll.insert_many(documents)
            ids = result.inserted_ids

        except BulkWriteError as bwe:
            print(f"Erro ao inserir documentos: {bwe.details}")
            return []

        return ids

    def read(self, query: dict = None) -> List[BaseModel]:
        query = query if query else {}

    def update(self, query: dict = None, update_data: dict = None) -> List[str]:
        query = query if query else {}

    def delete(self, model_id: str) -> Optional[BaseModel]:
        pass

    def list(self) -> List[BaseModel]:
        pass
