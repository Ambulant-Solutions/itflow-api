from itflow_api.models import Result, Client
from itflow_api.exceptions import ITFlowApiException
from typing import List

class AssetsModule:
    def __init__(self, rest_adapter):
        self._rest_adapter = rest_adapter