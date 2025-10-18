from ..exceptions import ITFlowApiException
from .contacts import ContactsModule
from typing import List, Optional
from datetime import datetime

class Client:
    client_id: Optional[int]
    client_lead: Optional[int]
    client_name: Optional[str]
    client_type: Optional[str]
    client_website: Optional[str]
    client_referral: Optional[str]
    client_rate: Optional[str]
    client_currency_code: Optional[str]
    client_net_terms: Optional[int]
    client_tax_id_number: Optional[str]
    client_abbreviation: Optional[str]
    client_notes: Optional[str]
    client_created_at: Optional[datetime]
    client_updated_at: Optional[datetime]
    client_archived_at: None
    client_accessed_at: Optional[datetime]

    def __init__(self, client_id: Optional[int], client_lead: Optional[int], client_name: Optional[str], client_type: Optional[str], client_website: Optional[str], client_referral: Optional[str], client_rate: Optional[str], client_currency_code: Optional[str], client_net_terms: Optional[int], client_tax_id_number: Optional[str], client_abbreviation: Optional[str], client_notes: Optional[str], client_created_at: Optional[datetime], client_updated_at: Optional[datetime], client_archived_at: None, client_accessed_at: Optional[datetime], **kwargs) -> None:
        self.client_id = client_id
        self.client_lead = client_lead
        self.client_name = client_name
        self.client_type = client_type
        self.client_website = client_website
        self.client_referral = client_referral
        self.client_rate = client_rate
        self.client_currency_code = client_currency_code
        self.client_net_terms = client_net_terms
        self.client_tax_id_number = client_tax_id_number
        self.client_abbreviation = client_abbreviation
        self.client_notes = client_notes
        self.client_created_at = client_created_at
        self.client_updated_at = client_updated_at
        self.client_archived_at = client_archived_at
        self.client_accessed_at = client_accessed_at
        self.__dict__.update(kwargs)

class ClientsModule:
    def __init__(self, rest_adapter):
        self._rest_adapter = rest_adapter

    def get_all_clients(self) -> List[Client]:
        """
        Fetch all clients from the IT Flow instance.
        :return: List object containing a list of Client objects
        """
        result = self._rest_adapter.get('clients')

        if result.status_code == 200:
            clients = [Client(**client_data) for client_data in result.data]
            return clients
        
        raise ITFlowApiException(f"Failed to fetch clients: {result.status_code} - {result.message}")
    
    def get_client_by_id(self, client_id: int) -> Client:
        """
        Fetch a single client by its ID.
        :param client_id: The ID of the client to fetch.
        :return: Client object
        """
        result = self._rest_adapter.get('clients', ep_params={'client_id': client_id})

        if result.status_code == 200 and result.data:
            return Client(**result.data[0])
        
        raise ITFlowApiException(f"Failed to fetch client with ID {client_id}: {result.status_code} - {result.message}")
    
    def create_client(self, client: Client) -> Client:
        """
        Create a new client in the IT Flow instance.
        :param client: Client object containing the details of the client to create.
        :return: Client object representing the newly created client.
        """
        client_data = client.__dict__.copy()
        client_data.pop('client_id', None)  # Remove client_id if present, as it will be assigned by the server.

        result = self._rest_adapter.create('clients', data=client_data)

        if result.status_code == 201 and result.data:
            return Client(**result.data[0])
        
        raise ITFlowApiException(f"Failed to create client: {result.status_code} - {result.message}")
    
    def update_client(self, client: Client) -> Client:
        """
        Update an existing client in the IT Flow instance.
        :param client: Client object containing the updated details of the client. Must include client_id.
        :return: Client object representing the updated client.
        """
        if not client.client_id:
            raise ValueError("Client ID is required for updating a client.")

        client_data = client.__dict__.copy()
        print(client_data)

        result = self._rest_adapter.update('clients', data=client_data)

        if result.status_code == 200 and result.data:
            return Client(**result.data[0])
        
        raise ITFlowApiException(f"Failed to update client with ID {client.client_id}: {result.status_code} - {result.message}")
    
    def delete_client(self, client_id: int) -> bool:
        """
        Delete a client from the IT Flow instance.
        :param client_id: The ID of the client to delete.
        :return: True if deletion was successful, False otherwise.
        """
        result = self._rest_adapter.delete('clients', data={'client_id': client_id})

        if result.status_code == 200:
            return True
        
        raise ITFlowApiException(f"Failed to delete client with ID {client_id}: {result.status_code} - {result.message}")
    
    def contacts(self):
        result = ContactsModule.get_contacts_by_client(self.client_id)
        return result
