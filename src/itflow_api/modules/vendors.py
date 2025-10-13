from itflow_api.models import Client
from itflow_api.exceptions import ITFlowApiException
from typing import List

class VendorsModule:
    def __init__(self, rest_adapter):
        self._rest_adapter = rest_adapter