import abc


class LightBase(abc.ABC):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def light_on(self):
        pass

    @abc.abstractmethod
    def light_off(self):
        pass
