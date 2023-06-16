from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesActivitiesIdEndpoint import SalesActivitiesIdEndpoint
from pywise.endpoints.SalesActivitiesCountEndpoint import SalesActivitiesCountEndpoint
from pywise.endpoints.SalesActivitiesStatusesEndpoint import SalesActivitiesStatusesEndpoint
from pywise.endpoints.SalesActivitiesTypesEndpoint import SalesActivitiesTypesEndpoint
from pywise.models.ActivityModel import ActivityModel

class SalesActivitiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "activities", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesActivitiesCountEndpoint(client, parent_endpoint=self)
        )
        self.statuses = self.register_child_endpoint(
            SalesActivitiesStatusesEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            SalesActivitiesTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesActivitiesIdEndpoint:
        child = SalesActivitiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ActivityModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ActivityModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ActivityModel]:
        return self._parse_many(ActivityModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ActivityModel:
        return self._parse_one(ActivityModel, super().make_request("POST", params=params))
        