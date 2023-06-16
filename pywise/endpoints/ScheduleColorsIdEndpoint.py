from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleColorsIdClearEndpoint import ScheduleColorsIdClearEndpoint
from pywise.models.ScheduleColorModel import ScheduleColorModel

class ScheduleColorsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.clear = self.register_child_endpoint(
            ScheduleColorsIdClearEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ScheduleColorModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ScheduleColorModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> ScheduleColorModel:
        return self._parse_one(ScheduleColorModel, super().make_request("GET", params=params))
        
    def put(self, data=None, params=None) -> ScheduleColorModel:
        return self._parse_one(ScheduleColorModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> ScheduleColorModel:
        return self._parse_one(ScheduleColorModel, super().make_request("PATCH", params=params))
        