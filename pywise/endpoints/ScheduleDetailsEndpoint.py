from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleDetailsIdEndpoint import ScheduleDetailsIdEndpoint
from pywise.endpoints.ScheduleDetailsCountEndpoint import ScheduleDetailsCountEndpoint
from pywise.models.ScheduleEntryDetailModel import ScheduleEntryDetailModel

class ScheduleDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleDetailsIdEndpoint:
        child = ScheduleDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ScheduleEntryDetailModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ScheduleEntryDetailModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ScheduleEntryDetailModel]:
        return self._parse_many(ScheduleEntryDetailModel, super().make_request("GET", params=params))
        