from abc import ABC, abstractmethod

class BaseRepositoryInterface(ABC):
    @abstractmethod
    def create(self, entity):
        """Insere uma nova entidade no repositório."""
        pass

    @abstractmethod
    def read(self, entity_id):
        """Lê uma entidade específica com base no ID."""
        pass

    @abstractmethod
    def update(self, entity):
        """Atualiza uma entidade existente no repositório."""
        pass

    @abstractmethod
    def delete(self, entity_id):
        """Remove uma entidade do repositório com base no ID."""
        pass

    @abstractmethod
    def list(self):
        """Lista todas as entidades no repositório."""
        pass
