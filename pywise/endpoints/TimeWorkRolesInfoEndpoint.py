from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.TimeWorkRolesInfoCountEndpoint import TimeWorkRolesInfoCountEndpoint
from pywise.models.WorkRoleInfoModel import WorkRoleInfoModel

class TimeWorkRolesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            TimeWorkRolesInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[WorkRoleInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            WorkRoleInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[WorkRoleInfoModel]:
        return self._parse_many(WorkRoleInfoModel, super().make_request("GET", params=params))
        