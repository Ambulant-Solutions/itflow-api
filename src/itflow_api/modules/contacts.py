from ..models import Contact
from ..exceptions import ITFlowApiException
from typing import List, Optional
from datetime import datetime

class Contact:
    contact_id: Optional[int]
    contact_name: Optional[str]
    contact_title: Optional[str]
    contact_email: Optional[str]
    contact_phone_country_code: Optional[str]
    contact_phone: Optional[str]
    contact_extension: Optional[str]
    contact_mobile_country_code: Optional[str]
    contact_mobile: Optional[str]
    contact_photo: None
    contact_notes: Optional[str]
    contact_primary: Optional[int]
    contact_important: Optional[int]
    contact_billing: Optional[int]
    contact_technical: Optional[int]
    contact_created_at: Optional[datetime]
    contact_updated_at: Optional[datetime]
    contact_archived_at: None
    contact_accessed_at: Optional[datetime]
    contact_location_id: Optional[int]
    contact_user_id: Optional[int]
    contact_department: Optional[str]
    contact_client_id: Optional[int]

    def __init__(self, contact_id: Optional[int], contact_name: Optional[str], contact_title: Optional[str], contact_email: Optional[str], contact_phone_country_code: Optional[str], contact_phone: Optional[str], contact_extension: Optional[str], contact_mobile_country_code: Optional[str], contact_mobile: Optional[str], contact_photo: None, contact_notes: Optional[str], contact_primary: Optional[int], contact_important: Optional[int], contact_billing: Optional[int], contact_technical: Optional[int], contact_created_at: Optional[datetime], contact_updated_at: Optional[datetime], contact_archived_at: None, contact_accessed_at: Optional[datetime], contact_location_id: Optional[int], contact_user_id: Optional[int], contact_department: Optional[str], contact_client_id: Optional[int], **kwargs) -> None:
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.contact_title = contact_title
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.contact_mobile = contact_mobile
        self.contact_photo = contact_photo
        self.contact_notes = contact_notes
        self.contact_primary = contact_primary
        self.contact_important = contact_important
        self.contact_billing = contact_billing
        self.contact_technical = contact_technical
        self.contact_created_at = contact_created_at
        self.contact_updated_at = contact_updated_at
        self.contact_archived_at = contact_archived_at
        self.contact_accessed_at = contact_accessed_at
        self.contact_location_id = contact_location_id
        self.contact_user_id = contact_user_id
        self.contact_department = contact_department
        self.contact_client_id = contact_client_id
        self.__dict__.update(kwargs)

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