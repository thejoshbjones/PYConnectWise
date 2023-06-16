from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemCwTimeZonesIdEndpoint import SystemCwTimeZonesIdEndpoint
from pywise.endpoints.SystemCwTimeZonesCountEndpoint import SystemCwTimeZonesCountEndpoint
from pywise.models.CwTimeZoneModel import CwTimeZoneModel

class SystemCwTimeZonesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "cwTimeZones", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemCwTimeZonesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemCwTimeZonesIdEndpoint:
        child = SystemCwTimeZonesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CwTimeZoneModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CwTimeZoneModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CwTimeZoneModel]:
        return self._parse_many(CwTimeZoneModel, super().make_request("GET", params=params))
        