from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeWorkTypesIdEndpoint import TimeWorkTypesIdEndpoint
from pywise.endpoints.TimeWorkTypesCountEndpoint import TimeWorkTypesCountEndpoint
from pywise.endpoints.TimeWorkTypesInfoEndpoint import TimeWorkTypesInfoEndpoint
from pywise.models.WorkTypeModel import WorkTypeModel

class TimeWorkTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeWorkTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            TimeWorkTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeWorkTypesIdEndpoint:
        child = TimeWorkTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WorkTypeModel]:
        return self._parse_many(WorkTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> WorkTypeModel:
        return self._parse_one(WorkTypeModel, super().make_request("POST", params=params))
        