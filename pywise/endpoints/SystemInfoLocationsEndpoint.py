from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInfoLocationsIdEndpoint import SystemInfoLocationsIdEndpoint
from pywise.endpoints.SystemInfoLocationsCountEndpoint import SystemInfoLocationsCountEndpoint
from pywise.models.LocationInfoModel import LocationInfoModel

class SystemInfoLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoLocationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInfoLocationsIdEndpoint:
        child = SystemInfoLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[LocationInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            LocationInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[LocationInfoModel]:
        return self._parse_many(LocationInfoModel, super().make_request("GET", params=params))
        