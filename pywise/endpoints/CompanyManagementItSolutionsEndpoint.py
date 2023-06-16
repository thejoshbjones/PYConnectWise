from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyManagementItSolutionsIdEndpoint import CompanyManagementItSolutionsIdEndpoint
from pywise.endpoints.CompanyManagementItSolutionsCountEndpoint import CompanyManagementItSolutionsCountEndpoint
from pywise.models.ManagementItSolutionModel import ManagementItSolutionModel

class CompanyManagementItSolutionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementItSolutions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagementItSolutionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyManagementItSolutionsIdEndpoint:
        child = CompanyManagementItSolutionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagementItSolutionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagementItSolutionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagementItSolutionModel]:
        return self._parse_many(ManagementItSolutionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ManagementItSolutionModel:
        return self._parse_one(ManagementItSolutionModel, super().make_request("POST", params=params))
        