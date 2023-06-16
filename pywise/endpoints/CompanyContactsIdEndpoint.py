from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyContactsIdImageEndpoint import CompanyContactsIdImageEndpoint
from pywise.endpoints.CompanyContactsIdPortalSecurityEndpoint import CompanyContactsIdPortalSecurityEndpoint
from pywise.endpoints.CompanyContactsIdUsagesEndpoint import CompanyContactsIdUsagesEndpoint
from pywise.endpoints.CompanyContactsIdCommunicationsEndpoint import CompanyContactsIdCommunicationsEndpoint
from pywise.endpoints.CompanyContactsIdGroupsEndpoint import CompanyContactsIdGroupsEndpoint
from pywise.endpoints.CompanyContactsIdNotesEndpoint import CompanyContactsIdNotesEndpoint
from pywise.endpoints.CompanyContactsIdTracksEndpoint import CompanyContactsIdTracksEndpoint
from pywise.endpoints.CompanyContactsIdTypeAssociationsEndpoint import CompanyContactsIdTypeAssociationsEndpoint
from pywise.models.ContactModel import ContactModel

class CompanyContactsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.image = self.register_child_endpoint(
            CompanyContactsIdImageEndpoint(client, parent_endpoint=self)
        )
        self.portalSecurity = self.register_child_endpoint(
            CompanyContactsIdPortalSecurityEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            CompanyContactsIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.communications = self.register_child_endpoint(
            CompanyContactsIdCommunicationsEndpoint(client, parent_endpoint=self)
        )
        self.groups = self.register_child_endpoint(
            CompanyContactsIdGroupsEndpoint(client, parent_endpoint=self)
        )
        self.notes = self.register_child_endpoint(
            CompanyContactsIdNotesEndpoint(client, parent_endpoint=self)
        )
        self.tracks = self.register_child_endpoint(
            CompanyContactsIdTracksEndpoint(client, parent_endpoint=self)
        )
        self.typeAssociations = self.register_child_endpoint(
            CompanyContactsIdTypeAssociationsEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ContactModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ContactModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> ContactModel:
        return self._parse_one(ContactModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> ContactModel:
        return self._parse_one(ContactModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> ContactModel:
        return self._parse_one(ContactModel, super().make_request("PATCH", params=params))
        