import logging

class LogGenerator:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename="./Logs/demo.log", mode="w")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
