from ..models import Contact
from ..exceptions import ITFlowApiException
from typing import List

class ContactsModule:
    def __init__(self, rest_adapter):
        self._rest_adapter = rest_adapter

    def get_all_contacts(self) -> List[Contact]:
        """
        Fetch all contacts from the IT Flow instance.
        :return: List object containing a list of Contact objects
        """
        result = self._rest_adapter.get('contacts')

        if result.status_code == 200:
            contacts = [Contact(**contact_data) for contact_data in result.data]
            return contacts
        
        raise ITFlowApiException(f"Failed to fetch contacts: {result.status_code} - {result.message}")
    
    def get_contact_by_id(self, contact_id: int) -> Contact:
        """
        Fetch a single contact by its ID.
        :param contact_id: The ID of the contact to fetch.
        :return: Contact object
        """
        result = self._rest_adapter.get('contacts', ep_params={'contact_id': contact_id})

        if result.status_code == 200 and result.data:
            return Contact(**result.data[0])
        
        raise ITFlowApiException(f"Failed to fetch contact with ID {contact_id}: {result.status_code} - {result.message}")