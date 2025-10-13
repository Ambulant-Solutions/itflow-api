import logging
from itflow_api.rest_adapter import RestAdapter
from itflow_api.exceptions import ITFlowApiException
from itflow_api.modules.clients import ClientsModule
from itflow_api.modules.contacts import ContactsModule
from itflow_api.modules.assets import AssetsModule

class ITFlowApi:
    def __init__(self, hostname: str, api_key: str, ver: str = 'v1', ssl_verify: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, api_key, ver, ssl_verify, logger)

        self.clients = ClientsModule(self._rest_adapter)
        self.contacts = ContactsModule(self._rest_adapter)
        self.assets = AssetsModule(self._rest_adapter)
        