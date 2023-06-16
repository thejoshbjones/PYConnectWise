from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeTimePeriodSetupsIdPeriodsIdEndpoint import TimeTimePeriodSetupsIdPeriodsIdEndpoint
from pywise.endpoints.TimeTimePeriodSetupsIdPeriodsCountEndpoint import TimeTimePeriodSetupsIdPeriodsCountEndpoint
from pywise.models.TimePeriodModel import TimePeriodModel

class TimeTimePeriodSetupsIdPeriodsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "periods", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeTimePeriodSetupsIdPeriodsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeTimePeriodSetupsIdPeriodsIdEndpoint:
        child = TimeTimePeriodSetupsIdPeriodsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TimePeriodModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TimePeriodModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TimePeriodModel]:
        return self._parse_many(TimePeriodModel, super().make_request("GET", params=params))
        