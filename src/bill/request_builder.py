__author__ = "zfoteff"
__version__ = "v0.0.1"

import os
import json
from typing import Tuple, Self

class RequestBuilder:
    def __init__(self):
        self.__query_params = dict()
        self.__path_params = dict()

    def build(self) -> Tuple:
        pass

    def add_path_param(key: str, value: any) -> Self:
        pass

    def add_path_params():
        pass 