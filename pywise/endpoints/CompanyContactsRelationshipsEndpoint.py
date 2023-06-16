from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyContactsRelationshipsIdEndpoint import CompanyContactsRelationshipsIdEndpoint
from pywise.endpoints.CompanyContactsRelationshipsCountEndpoint import CompanyContactsRelationshipsCountEndpoint
from pywise.models.ContactRelationshipModel import ContactRelationshipModel

class CompanyContactsRelationshipsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "relationships", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsRelationshipsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyContactsRelationshipsIdEndpoint:
        child = CompanyContactsRelationshipsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ContactRelationshipModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ContactRelationshipModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ContactRelationshipModel]:
        return self._parse_many(ContactRelationshipModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ContactRelationshipModel:
        return self._parse_one(ContactRelationshipModel, super().make_request("POST", params=params))
        