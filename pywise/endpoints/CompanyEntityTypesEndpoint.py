from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyEntityTypesIdEndpoint import CompanyEntityTypesIdEndpoint
from pywise.endpoints.CompanyEntityTypesCountEndpoint import CompanyEntityTypesCountEndpoint
from pywise.models.EntityTypeModel import EntityTypeModel

class CompanyEntityTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "entityTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyEntityTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyEntityTypesIdEndpoint:
        child = CompanyEntityTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[EntityTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            EntityTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[EntityTypeModel]:
        return self._parse_many(EntityTypeModel, super().make_request("GET", params=params))
        