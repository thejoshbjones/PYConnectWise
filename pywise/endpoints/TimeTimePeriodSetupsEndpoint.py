from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeTimePeriodSetupsIdEndpoint import TimeTimePeriodSetupsIdEndpoint
from pywise.endpoints.TimeTimePeriodSetupsCountEndpoint import TimeTimePeriodSetupsCountEndpoint
from pywise.endpoints.TimeTimePeriodSetupsDefaultEndpoint import TimeTimePeriodSetupsDefaultEndpoint
from pywise.models.TimePeriodSetupModel import TimePeriodSetupModel

class TimeTimePeriodSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "timePeriodSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeTimePeriodSetupsCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            TimeTimePeriodSetupsDefaultEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeTimePeriodSetupsIdEndpoint:
        child = TimeTimePeriodSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TimePeriodSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TimePeriodSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TimePeriodSetupModel]:
        return self._parse_many(TimePeriodSetupModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TimePeriodSetupModel:
        return self._parse_one(TimePeriodSetupModel, super().make_request("POST", params=params))
        