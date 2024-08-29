from . import BaseRepositoryInterface
from ..models import UserModelInterface
from typing import List, Optional, Union
from abc import abstractmethod

class UserRepositoryInterface(BaseRepositoryInterface):
    @abstractmethod
    def get_by_id(self, user_id: str) -> Optional[UserModelInterface]:
        """
        Obtém o usúario através do ID.

        Retorna None caso não encontre.
        """
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UserModelInterface]:
        """
        Obtém o usúario através do email.

        Retorna None caso não encontre.
        """
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> List[UserModelInterface]:
        """
        Obtém uma lista de usúarios através do username
        """
        pass

    @abstractmethod
    def save_user(self, users: Union[List[UserModelInterface], UserModelInterface]) -> List[str]:
        """
        Salva os dados dos UserModels passados no UserRepository.

        Retorna uma lista de IDs dos usuários salvos.
        """
        pass
