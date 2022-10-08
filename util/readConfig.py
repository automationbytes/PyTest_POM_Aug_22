import configparser

config = configparser.RawConfigParser()
config.read('./Configurations/config.ini')

class readConfig:

    @staticmethod
    def getUrl():
        url = config.get('commoninfo','baseURL')
        return url