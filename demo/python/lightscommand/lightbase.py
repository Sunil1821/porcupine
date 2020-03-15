import abc


class LightBase(abc.ABC):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def invoke(self):
        pass
