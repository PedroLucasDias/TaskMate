from . import BaseModelInterface
from abc import abstractmethod

class UserModelInterface(BaseModelInterface):
    @property
    @abstractmethod
    def user_name(self) -> str:
        """Obtém o nome de usuário."""
        pass

    @user_name.setter
    @abstractmethod
    def user_name(self, value: str):
        """Define o nome de usuário."""
        pass

    @property
    @abstractmethod
    def password(self) -> str:
        """Obtém a senha do usuário."""
        pass

    @password.setter
    @abstractmethod
    def password(self, value: str):
        """Define a senha do usuário."""
        pass

    @property
    @abstractmethod
    def email(self) -> str:
        """Obtém o email do usuário."""
        pass

    @email.setter
    @abstractmethod
    def email(self, value: str):
        """Define o email do usuário."""
        pass

    @property
    @abstractmethod
    def tasks(self) -> list:
        """Obtém a lista de tasks do usuário."""
        pass

    @tasks.setter
    @abstractmethod
    def tasks(self, value: list):
        """Define a lsita de tasks do usuário."""
        pass
