from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeSheetsIdEndpoint import TimeSheetsIdEndpoint
from pywise.endpoints.TimeSheetsCountEndpoint import TimeSheetsCountEndpoint
from pywise.models.TimeSheetModel import TimeSheetModel

class TimeSheetsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "sheets", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeSheetsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeSheetsIdEndpoint:
        child = TimeSheetsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TimeSheetModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TimeSheetModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TimeSheetModel]:
        return self._parse_many(TimeSheetModel, super().make_request("GET", params=params))
        