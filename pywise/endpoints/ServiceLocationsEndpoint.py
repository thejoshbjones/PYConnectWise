from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceLocationsIdEndpoint import ServiceLocationsIdEndpoint
from pywise.endpoints.ServiceLocationsCountEndpoint import ServiceLocationsCountEndpoint
from pywise.endpoints.ServiceLocationsInfoEndpoint import ServiceLocationsInfoEndpoint
from pywise.models.ServiceLocationModel import ServiceLocationModel

class ServiceLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceLocationsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ServiceLocationsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceLocationsIdEndpoint:
        child = ServiceLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ServiceLocationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ServiceLocationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ServiceLocationModel]:
        return self._parse_many(ServiceLocationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ServiceLocationModel:
        return self._parse_one(ServiceLocationModel, super().make_request("POST", params=params))
        