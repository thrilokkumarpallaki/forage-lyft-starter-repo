from abc import ABC, abstractmethod

from serviceable import Serviceable


class Battery(Serviceable, ABC):
    @abstractmethod
    def need_service(self) -> bool:
        pass
