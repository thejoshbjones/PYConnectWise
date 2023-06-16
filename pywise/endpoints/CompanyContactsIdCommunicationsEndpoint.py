from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyContactsIdCommunicationsIdEndpoint import CompanyContactsIdCommunicationsIdEndpoint
from pywise.endpoints.CompanyContactsIdCommunicationsCountEndpoint import CompanyContactsIdCommunicationsCountEndpoint
from pywise.models.ContactCommunicationModel import ContactCommunicationModel

class CompanyContactsIdCommunicationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "communications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsIdCommunicationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyContactsIdCommunicationsIdEndpoint:
        child = CompanyContactsIdCommunicationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ContactCommunicationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ContactCommunicationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ContactCommunicationModel]:
        return self._parse_many(ContactCommunicationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ContactCommunicationModel:
        return self._parse_one(ContactCommunicationModel, super().make_request("POST", params=params))
        