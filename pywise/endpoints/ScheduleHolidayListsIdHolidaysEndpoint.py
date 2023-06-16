from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleHolidayListsIdHolidaysIdEndpoint import ScheduleHolidayListsIdHolidaysIdEndpoint
from pywise.endpoints.ScheduleHolidayListsIdHolidaysCountEndpoint import ScheduleHolidayListsIdHolidaysCountEndpoint
from pywise.models.HolidayModel import HolidayModel

class ScheduleHolidayListsIdHolidaysEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "holidays", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleHolidayListsIdHolidaysCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleHolidayListsIdHolidaysIdEndpoint:
        child = ScheduleHolidayListsIdHolidaysIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[HolidayModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            HolidayModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[HolidayModel]:
        return self._parse_many(HolidayModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> HolidayModel:
        return self._parse_one(HolidayModel, super().make_request("POST", params=params))
        