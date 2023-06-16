from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleHolidayListsIdEndpoint import ScheduleHolidayListsIdEndpoint
from pywise.endpoints.ScheduleHolidayListsCopyEndpoint import ScheduleHolidayListsCopyEndpoint
from pywise.endpoints.ScheduleHolidayListsCountEndpoint import ScheduleHolidayListsCountEndpoint
from pywise.models.HolidayListModel import HolidayListModel

class ScheduleHolidayListsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "holidayLists", parent_endpoint=parent_endpoint)
        
        self.copy = self.register_child_endpoint(
            ScheduleHolidayListsCopyEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            ScheduleHolidayListsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleHolidayListsIdEndpoint:
        child = ScheduleHolidayListsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[HolidayListModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            HolidayListModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[HolidayListModel]:
        return self._parse_many(HolidayListModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> HolidayListModel:
        return self._parse_one(HolidayListModel, super().make_request("POST", params=params))
        