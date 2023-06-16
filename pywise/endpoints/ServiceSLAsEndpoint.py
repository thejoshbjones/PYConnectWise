from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceSLAsIdEndpoint import ServiceSLAsIdEndpoint
from pywise.endpoints.ServiceSLAsCountEndpoint import ServiceSLAsCountEndpoint
from pywise.models.SLAModel import SLAModel

class ServiceSLAsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "SLAs", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceSLAsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceSLAsIdEndpoint:
        child = ServiceSLAsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SLAModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SLAModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SLAModel]:
        return self._parse_many(SLAModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SLAModel:
        return self._parse_one(SLAModel, super().make_request("POST", params=params))
        