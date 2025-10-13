import logging
from .rest_adapter import RestAdapter
from .exceptions import ITFlowApiException
from .modules.assets import AssetsModule
from .modules.certificates import CertificatesModule
from .modules.clients import ClientsModule
from .modules.contacts import ContactsModule
from .modules.credentials import CredentialsModule
from .modules.documents import DocumentsModule
from .modules.domains import DomainsModule
from .modules.expenses import ExpensesModule
from .modules.invoices import InvoicesModule
from .modules.locations import LocationsModule
from .modules.networks import NetworksModule
from .modules.payments import PaymentsModule
from .modules.products import ProductsModule
from .modules.software import SoftwareModule
from .modules.tickets import TicketsModule
from .modules.vendors import VendorsModule

class ITFlowApi:
    def __init__(self, hostname: str, api_key: str, ver: str = 'v1', ssl_verify: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, api_key, ver, ssl_verify, logger)

        self.assets = AssetsModule(self._rest_adapter)
        self.certificates = CertificatesModule(self._rest_adapter)
        self.clients = ClientsModule(self._rest_adapter)
        self.contacts = ContactsModule(self._rest_adapter)
        self.credentials = CredentialsModule(self._rest_adapter)
        self.documents = DocumentsModule(self._rest_adapter)
        self.domains = DomainsModule(self._rest_adapter)
        self.expenses = ExpensesModule(self._rest_adapter)
        self.invoices = InvoicesModule(self._rest_adapter)
        self.locations = LocationsModule(self._rest_adapter)
        self.networks = NetworksModule(self._rest_adapter)
        self.payments = PaymentsModule(self._rest_adapter)
        self.products = ProductsModule(self._rest_adapter)
        self.software = SoftwareModule(self._rest_adapter)
        self.tickets = TicketsModule(self._rest_adapter)
        self.vendors = VendorsModule(self._rest_adapter)
        
