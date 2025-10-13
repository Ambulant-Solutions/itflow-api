from ..models import Client
from ..exceptions import ITFlowApiException
from typing import List

class VendorsModule:
    def __init__(self, rest_adapter):
        self._rest_adapter = rest_adapter