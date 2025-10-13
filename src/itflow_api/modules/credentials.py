from ..models import Client
from ..exceptions import ITFlowApiException
from typing import List

class CredentialsModule:
    def __init__(self, rest_adapter):
        self._rest_adapter = rest_adapter