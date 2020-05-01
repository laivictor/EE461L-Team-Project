import mongodb
import abc


class DataStrategy(abc.ABC):
    @abc.abstractmethod
    def getData(self):
        pass


class Countries(DataStrategy):
    instance = None

    def __init__(self):
        Countries.instance = self

    @staticmethod
    def getInstance():
        if Countries.instance == None:
            Countries()
        return Countries.instance
    
    def getData(self):
        return mongodb.getCountries()


class HostCities(DataStrategy):
    instance = None

    def __init__(self):
        HostCities.instance = self

    @staticmethod
    def getInstance():
        if HostCities.instance == None:
            HostCities()
        return HostCities.instance
    
    def getData(self):
        return mongodb.getHostCities()


class Module():    
    module = None

    def __init__(self, module):
        self.module = module
    
    def data(self):
        return self.module.getData()