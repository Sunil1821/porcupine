import abc


class UnderstandBase(abc.ABC):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def listen(self):
        pass