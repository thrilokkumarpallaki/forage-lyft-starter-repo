from abc import ABC, abstractmethod


class Tire(ABC):
    @abstractmethod
    def need_service(self):
        pass
