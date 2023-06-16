from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesActivitiesTypesIdEndpoint import SalesActivitiesTypesIdEndpoint
from pywise.endpoints.SalesActivitiesTypesCountEndpoint import SalesActivitiesTypesCountEndpoint
from pywise.models.ActivityTypeModel import ActivityTypeModel

class SalesActivitiesTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesActivitiesTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesActivitiesTypesIdEndpoint:
        child = SalesActivitiesTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ActivityTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ActivityTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ActivityTypeModel]:
        return self._parse_many(ActivityTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ActivityTypeModel:
        return self._parse_one(ActivityTypeModel, super().make_request("POST", params=params))
        