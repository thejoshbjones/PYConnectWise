from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeWorkRolesIdLocationsIdEndpoint import TimeWorkRolesIdLocationsIdEndpoint
from pywise.endpoints.TimeWorkRolesIdLocationsCountEndpoint import TimeWorkRolesIdLocationsCountEndpoint
from pywise.models.WorkRoleLocationModel import WorkRoleLocationModel

class TimeWorkRolesIdLocationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "locations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeWorkRolesIdLocationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeWorkRolesIdLocationsIdEndpoint:
        child = TimeWorkRolesIdLocationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkRoleLocationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkRoleLocationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WorkRoleLocationModel]:
        return self._parse_many(WorkRoleLocationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> WorkRoleLocationModel:
        return self._parse_one(WorkRoleLocationModel, super().make_request("POST", params=params))
        