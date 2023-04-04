__author__ = "zfoteff"
__version__ = "v0.0.1"

import os
import requests
import json
from bin.constants import API_KEY
from typing import Self

class CongressAPIClient:
    def __init__(self) -> Self:
        self.__base_url = "https://api.congress.gov"
        self.__api_version = "v3"
        self.__
    
    @property
    def base_url(self) -> None:
        return self.__base_url
    
    @property
    def api_version(self) -> None:
        return self.__api_version

    @property
    def full_url(self) -> str:
        return f"{self.__base_url}/{self.__api_version}/"
    
    def 