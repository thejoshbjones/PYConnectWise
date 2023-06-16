from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyContactsTypesIdEndpoint import CompanyContactsTypesIdEndpoint
from pywise.endpoints.CompanyContactsTypesCountEndpoint import CompanyContactsTypesCountEndpoint
from pywise.endpoints.CompanyContactsTypesInfoEndpoint import CompanyContactsTypesInfoEndpoint
from pywise.models.ContactTypeModel import ContactTypeModel

class CompanyContactsTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyContactsTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyContactsTypesIdEndpoint:
        child = CompanyContactsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ContactTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ContactTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ContactTypeModel]:
        return self._parse_many(ContactTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ContactTypeModel:
        return self._parse_one(ContactTypeModel, super().make_request("POST", params=params))
        