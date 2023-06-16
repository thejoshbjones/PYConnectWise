from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeWorkRolesIdEndpoint import TimeWorkRolesIdEndpoint
from pywise.endpoints.TimeWorkRolesCountEndpoint import TimeWorkRolesCountEndpoint
from pywise.endpoints.TimeWorkRolesInfoEndpoint import TimeWorkRolesInfoEndpoint
from pywise.models.WorkRoleModel import WorkRoleModel

class TimeWorkRolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workRoles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeWorkRolesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            TimeWorkRolesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> TimeWorkRolesIdEndpoint:
        child = TimeWorkRolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkRoleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkRoleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WorkRoleModel]:
        return self._parse_many(WorkRoleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> WorkRoleModel:
        return self._parse_one(WorkRoleModel, super().make_request("POST", params=params))
        