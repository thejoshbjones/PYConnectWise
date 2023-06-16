from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemLocationsIdEndpoint import SystemLocationsIdEndpoint
from pywise.endpoints.SystemLocationsCountEndpoint import SystemLocationsCountEndpoint
from pywise.models.LocationModel import LocationModel

class SystemLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemLocationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemLocationsIdEndpoint:
        child = SystemLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[LocationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            LocationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[LocationModel]:
        return self._parse_many(LocationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> LocationModel:
        return self._parse_one(LocationModel, super().make_request("POST", params=params))
        