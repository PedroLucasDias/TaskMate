from abc import ABC, abstractmethod
from typing import List, Optional, Union

from ..models import BaseModelInterface


class BaseRepositoryInterface(ABC):
    @abstractmethod
    def create(self, *models: BaseModelInterface) -> List[str]:
        """
        Insere os dados de um ou mais Models no repositório.

        Retorna os IDs.
        """
        pass

    @abstractmethod
    def read(self, query: dict = None) -> List[BaseModelInterface]:
        """
        Retorna uma lista de Models com base na query.
        """
        pass

    @abstractmethod
    def update(self, query: dict = None, update_data: dict = None) -> List[str]:
        """
        Atualiza os dados no repositório de acordo com a query.

        Retorna retorna uma lista com os IDs dos dados alterados.

        Se nenhuma query ou update_data for fornecida, não realiza nenhuma atualização.
        """
        pass

    @abstractmethod
    def delete(self, model_id: str) -> Optional[BaseModelInterface]:
        """
        Remove uma entidade do repositório com base no ID.

        Retorna os dados removidos do repositório ou None casa não seja possível.
        """
        pass

    @abstractmethod
    def list(self) -> List[BaseModelInterface]:
        """
        Lista todas as entidades no repositório.
        """
        pass
