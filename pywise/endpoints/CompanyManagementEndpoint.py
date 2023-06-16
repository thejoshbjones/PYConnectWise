from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyManagementIdEndpoint import CompanyManagementIdEndpoint
from pywise.endpoints.CompanyManagementCountEndpoint import CompanyManagementCountEndpoint
from pywise.models.ManagementModel import ManagementModel

class CompanyManagementEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "management", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagementCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyManagementIdEndpoint:
        child = CompanyManagementIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagementModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagementModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagementModel]:
        return self._parse_many(ManagementModel, super().make_request("GET", params=params))
        