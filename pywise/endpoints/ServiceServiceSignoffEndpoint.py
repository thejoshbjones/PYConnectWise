from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceServiceSignoffIdEndpoint import ServiceServiceSignoffIdEndpoint
from pywise.endpoints.ServiceServiceSignoffCountEndpoint import ServiceServiceSignoffCountEndpoint
from pywise.endpoints.ServiceServiceSignoffInfoEndpoint import ServiceServiceSignoffInfoEndpoint
from pywise.models.ServiceSignoffModel import ServiceSignoffModel

class ServiceServiceSignoffEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "serviceSignoff", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceServiceSignoffCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceServiceSignoffInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceServiceSignoffIdEndpoint:
        child = ServiceServiceSignoffIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ServiceSignoffModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ServiceSignoffModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ServiceSignoffModel]:
        return self._parse_many(ServiceSignoffModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ServiceSignoffModel:
        return self._parse_one(ServiceSignoffModel, super().make_request("POST", params=params))
        