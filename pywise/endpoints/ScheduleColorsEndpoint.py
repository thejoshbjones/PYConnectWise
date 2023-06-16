from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleColorsIdEndpoint import ScheduleColorsIdEndpoint
from pywise.endpoints.ScheduleColorsCountEndpoint import ScheduleColorsCountEndpoint
from pywise.endpoints.ScheduleColorsResetEndpoint import ScheduleColorsResetEndpoint
from pywise.models.ScheduleColorModel import ScheduleColorModel

class ScheduleColorsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "colors", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleColorsCountEndpoint(client, parent_endpoint=self)
        )
        self.reset = self.register_child_endpoint(
            ScheduleColorsResetEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleColorsIdEndpoint:
        child = ScheduleColorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
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
    
    def get(self, data=None, params=None) -> list[ScheduleColorModel]:
        return self._parse_many(ScheduleColorModel, super().make_request("GET", params=params))
        