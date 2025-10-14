from ..models import Client
from ..exceptions import ITFlowApiException
from typing import List, Optional
from datetime import datetime


class Domain:
    domain_id: Optional[int]
    domain_name: Optional[str]
    domain_description: Optional[str]
    domain_expire: Optional[datetime]
    domain_ip: Optional[str]
    domain_name_servers: Optional[str]
    domain_mail_servers: Optional[str]
    domain_txt: Optional[str]
    domain_raw_whois: Optional[str]
    domain_notes: Optional[str]
    domain_created_at: Optional[datetime]
    domain_updated_at: Optional[datetime]
    domain_archived_at: None
    domain_accessed_at: None
    domain_registrar: Optional[int]
    domain_webhost: Optional[int]
    domain_dnshost: Optional[int]
    domain_mailhost: Optional[int]
    domain_client_id: Optional[int]

    def __init__(self, domain_id: Optional[int], domain_name: Optional[str], domain_description: Optional[str], domain_expire: Optional[datetime], domain_ip: Optional[str], domain_name_servers: Optional[str], domain_mail_servers: Optional[str], domain_txt: Optional[str], domain_raw_whois: Optional[str], domain_notes: Optional[str], domain_created_at: Optional[datetime], domain_updated_at: Optional[datetime], domain_archived_at: None, domain_accessed_at: None, domain_registrar: Optional[int], domain_webhost: Optional[int], domain_dnshost: Optional[int], domain_mailhost: Optional[int], domain_client_id: Optional[int], **kwargs) -> None:
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.domain_description = domain_description
        self.domain_expire = domain_expire
        self.domain_ip = domain_ip
        self.domain_name_servers = domain_name_servers
        self.domain_mail_servers = domain_mail_servers
        self.domain_txt = domain_txt
        self.domain_raw_whois = domain_raw_whois
        self.domain_notes = domain_notes
        self.domain_created_at = domain_created_at
        self.domain_updated_at = domain_updated_at
        self.domain_archived_at = domain_archived_at
        self.domain_accessed_at = domain_accessed_at
        self.domain_registrar = domain_registrar
        self.domain_webhost = domain_webhost
        self.domain_dnshost = domain_dnshost
        self.domain_mailhost = domain_mailhost
        self.domain_client_id = domain_client_id
        self.__dict__.update(kwargs)


class DomainsModule:
    def __init__(self, rest_adapter):
        self._rest_adapter = rest_adapter

    def get_all_domains(self) -> List[Domain]:
        """
        Fetch all domains from the IT Flow instance.
        :return: List object containing a list of Domain objects
        """
        result = self._rest_adapter.get('domains')

        if result.status_code == 200:
            domains = [Domain(**domain_data) for domain_data in result.data]
            return domains
        
        raise ITFlowApiException(f"Failed to fetch domains: {result.status_code} - {result.message}")
    
    def get_domain_by_id(self, domain_id: int) -> Domain:
        """
        Fetch a single domain by its ID.
        :param domain_id: The ID of the domain to fetch.
        :return: Domain object
        """
        result = self._rest_adapter.get('clients', ep_params={'domain_id': domain_id})

        if result.status_code == 200 and result.data:
            return Domain(**result.data[0])
        
        raise ITFlowApiException(f"Failed to fetch domain with ID {domain_id}: {result.status_code} - {result.message}")
    
    def get_domain_by_name(self, domain_name: str) -> Domain:
        """
        Fetch a single domain by its name.
        :param domain_name: The fully qualified domain name of the domain to fetch.
        :return: Domain object
        """
        result = self._rest_adapter.get('clients', ep_params={'domain_name': domain_name})

        if result.status_code == 200 and result.data:
            return Domain(**result.data[0])
        
        raise ITFlowApiException(f"Failed to fetch domain with name {domain_name}: {result.status_code} - {result.message}")