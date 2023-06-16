from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemSettingsIdEndpoint import SystemSettingsIdEndpoint
from pywise.endpoints.SystemSettingsCountEndpoint import SystemSettingsCountEndpoint
from pywise.models.SystemSettingModel import SystemSettingModel

class SystemSettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "settings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSettingsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemSettingsIdEndpoint:
        child = SystemSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SystemSettingModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SystemSettingModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SystemSettingModel]:
        return self._parse_many(SystemSettingModel, super().make_request("GET", params=params))
        