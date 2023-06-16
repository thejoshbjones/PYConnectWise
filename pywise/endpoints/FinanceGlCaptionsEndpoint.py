from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceGlCaptionsIdEndpoint import FinanceGlCaptionsIdEndpoint
from pywise.endpoints.FinanceGlCaptionsCountEndpoint import FinanceGlCaptionsCountEndpoint
from pywise.models.GLCaptionModel import GLCaptionModel

class FinanceGlCaptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "glCaptions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceGlCaptionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceGlCaptionsIdEndpoint:
        child = FinanceGlCaptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[GLCaptionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            GLCaptionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[GLCaptionModel]:
        return self._parse_many(GLCaptionModel, super().make_request("GET", params=params))
        