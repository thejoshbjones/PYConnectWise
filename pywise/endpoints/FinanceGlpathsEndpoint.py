from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceGlpathsIdEndpoint import FinanceGlpathsIdEndpoint
from pywise.endpoints.FinanceGlpathsCountEndpoint import FinanceGlpathsCountEndpoint
from pywise.models.GLPathModel import GLPathModel

class FinanceGlpathsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "glpaths", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceGlpathsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceGlpathsIdEndpoint:
        child = FinanceGlpathsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[GLPathModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            GLPathModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[GLPathModel]:
        return self._parse_many(GLPathModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> GLPathModel:
        return self._parse_one(GLPathModel, super().make_request("POST", params=params))
        