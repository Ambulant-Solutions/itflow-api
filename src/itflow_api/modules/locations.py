from ..models import Client
from ..exceptions import ITFlowApiException
from typing import List

class LocationsModule:
    def __init__(self, rest_adapter):
        self._rest_adapter = rest_adapter