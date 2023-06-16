from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServicePrioritiesIdEndpoint import ServicePrioritiesIdEndpoint
from pywise.endpoints.ServicePrioritiesCountEndpoint import ServicePrioritiesCountEndpoint
from pywise.models.PriorityModel import PriorityModel

class ServicePrioritiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "priorities", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServicePrioritiesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServicePrioritiesIdEndpoint:
        child = ServicePrioritiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PriorityModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PriorityModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PriorityModel]:
        return self._parse_many(PriorityModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PriorityModel:
        return self._parse_one(PriorityModel, super().make_request("POST", params=params))
        