from abc import ABC, abstractmethod

from serviceable import Serviceable


class Engine(Serviceable, ABC):
    @abstractmethod
    def need_service(self) -> bool:
        pass
