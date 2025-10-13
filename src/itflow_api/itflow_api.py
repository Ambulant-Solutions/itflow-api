import logging
from .rest_adapter import RestAdapter
from .exceptions import ITFlowApiException
from .modules.clients import ClientsModule
from .modules.contacts import ContactsModule
from .modules.assets import AssetsModule
from .modules.certificates import CertificatesModule
from .modules.credentials import CredentialsModule
from .modules.documents import DocumentsModule

class ITFlowApi:
    def __init__(self, hostname: str, api_key: str, ver: str = 'v1', ssl_verify: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, api_key, ver, ssl_verify, logger)

        self.assets = AssetsModule(self._rest_adapter)
        self.certificates = CertificatesModule(self._rest_adapter)
        self.clients = ClientsModule(self._rest_adapter)
        self.contacts = ContactsModule(self._rest_adapter)
        self.credentials = CredentialsModule(self._rest_adapter)
        self.documents = DocumentsModule(self._rest_adapter)
        
