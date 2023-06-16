from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyContactsIdGroupsIdEndpoint import CompanyContactsIdGroupsIdEndpoint
from pywise.endpoints.CompanyContactsIdGroupsCountEndpoint import CompanyContactsIdGroupsCountEndpoint
from pywise.models.ContactGroupModel import ContactGroupModel

class CompanyContactsIdGroupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "groups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsIdGroupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyContactsIdGroupsIdEndpoint:
        child = CompanyContactsIdGroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ContactGroupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ContactGroupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ContactGroupModel]:
        return self._parse_many(ContactGroupModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ContactGroupModel:
        return self._parse_one(ContactGroupModel, super().make_request("POST", params=params))
        