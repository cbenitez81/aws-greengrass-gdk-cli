import abc


class Recipe(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self) -> dict:
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def write(self, content) -> None:
        """Load in the data set"""
        raise NotImplementedError
