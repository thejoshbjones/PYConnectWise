from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ScheduleTypesIdEndpoint import ScheduleTypesIdEndpoint
from pywise.endpoints.ScheduleTypesCountEndpoint import ScheduleTypesCountEndpoint
from pywise.endpoints.ScheduleTypesInfoEndpoint import ScheduleTypesInfoEndpoint
from pywise.models.ScheduleTypeModel import ScheduleTypeModel

class ScheduleTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "types", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ScheduleTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ScheduleTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ScheduleTypesIdEndpoint:
        child = ScheduleTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ScheduleTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ScheduleTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ScheduleTypeModel]:
        return self._parse_many(ScheduleTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ScheduleTypeModel:
        return self._parse_one(ScheduleTypeModel, super().make_request("POST", params=params))
        