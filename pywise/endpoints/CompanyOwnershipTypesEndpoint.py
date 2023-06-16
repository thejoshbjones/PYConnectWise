from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyOwnershipTypesIdEndpoint import CompanyOwnershipTypesIdEndpoint
from pywise.endpoints.CompanyOwnershipTypesCountEndpoint import CompanyOwnershipTypesCountEndpoint
from pywise.endpoints.CompanyOwnershipTypesInfoEndpoint import CompanyOwnershipTypesInfoEndpoint
from pywise.models.OwnershipTypeModel import OwnershipTypeModel

class CompanyOwnershipTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "ownershipTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyOwnershipTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyOwnershipTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyOwnershipTypesIdEndpoint:
        child = CompanyOwnershipTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OwnershipTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OwnershipTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OwnershipTypeModel]:
        return self._parse_many(OwnershipTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> OwnershipTypeModel:
        return self._parse_one(OwnershipTypeModel, super().make_request("POST", params=params))
        