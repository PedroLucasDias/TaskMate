from . import BaseRepositoryInterface
from ..models import UserModelInterface
from typing import List
from abc import abstractmethod

class UserRepositoryInterface(BaseRepositoryInterface):
    @abstractmethod
    def get_by_id(self, id: str) -> UserModelInterface:
        """Obtém o usúario através do id"""
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserModelInterface:
        """Obtém o usúario através do email"""
        pass

    @abstractmethod
    def get_by_username(self, id: str) -> List[UserModelInterface]:
        """Obtém uma lista de usúarios através do username"""
        pass
