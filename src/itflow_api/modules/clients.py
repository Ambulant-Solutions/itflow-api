from itflow_api.models import Client
from itflow_api.exceptions import ITFlowApiException
from typing import List

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