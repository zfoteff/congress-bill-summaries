import os
import enum
import logging as log
 
LOG_DIR = str(os.getcwd()) + "\\logs\\"

class CongressLogger():
    def __log_setup(self, logger_name: str, log_file: str, mode: str="w", level: str="") -> log.Logger:
        formatter = log.Formatter("[%(levelname)s]\t[%(asctime)s] | %(name)s %(module)s %(message)s")
        file_handler = log.FileHandler(log_file, mode=mode)
        file_handler.setFormatter(formatter)
        stream_handler = log.StreamHandler()

        new_log = log.getLogger(logger_name)
        new_log.addHandler(file_handler)
        new_log.addHandler(stream_handler)
        return new_log
    
    def __init__(self, logger_name: str) -> None:
        self.__logger_name = logger_name
        self.__log_dir = LOG_DIR+f"{__logger_name}"
        self.__log_obj = self.__log_setup(logger_name=__logger_name, log_file=__log_dir)

    def __call__(self, log_str: str, mode: str = 'i') -> None:
        if mode == "i":
            self.__log_obj.info(log_str)