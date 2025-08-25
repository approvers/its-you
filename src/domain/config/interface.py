from abc import abstractmethod
from datetime import timedelta

from src.config.interface import ConfigIF


# noinspection PyPep8Naming
class DomainConfigIF(ConfigIF):
    @property
    @abstractmethod
    def REACT_PROBABILITY(self) -> float:
        pass

    @property
    @abstractmethod
    def INTERVAL_FOR_SAME_TARGET_SEC(self) -> timedelta:
        pass

    @property
    @abstractmethod
    def DO_REACT_TO_GROUP(self) -> bool:
        pass

    @property
    @abstractmethod
    def DO_REACT_TO_USER(self) -> bool:
        pass
