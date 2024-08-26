from abc import ABC, abstractmethod

class BaseModelInterface(ABC):
    @abstractmethod
    def load_json(self, json_data: str):
        """Carrega os dados de uma string JSON para o modelo."""
        pass

    @abstractmethod
    def to_json(self) -> str:
        """Converte os dados do modelo para uma string JSON."""
        pass

    @abstractmethod
    def load_dict(self, data: dict):
        """Carrega os dados de um dicionário para o modelo."""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Converte os dados do modelo para um dicionário."""
        pass
