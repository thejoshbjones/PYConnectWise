from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemTimeZoneSetupsIdEndpoint import SystemTimeZoneSetupsIdEndpoint
from pywise.endpoints.SystemTimeZoneSetupsCountEndpoint import SystemTimeZoneSetupsCountEndpoint
from pywise.endpoints.SystemTimeZoneSetupsInfoEndpoint import SystemTimeZoneSetupsInfoEndpoint
from pywise.models.TimeZoneSetupModel import TimeZoneSetupModel

class SystemTimeZoneSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "timeZoneSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemTimeZoneSetupsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SystemTimeZoneSetupsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemTimeZoneSetupsIdEndpoint:
        child = SystemTimeZoneSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TimeZoneSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TimeZoneSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TimeZoneSetupModel]:
        return self._parse_many(TimeZoneSetupModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TimeZoneSetupModel:
        return self._parse_one(TimeZoneSetupModel, super().make_request("POST", params=params))
        