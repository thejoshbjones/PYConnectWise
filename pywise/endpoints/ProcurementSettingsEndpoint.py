from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProcurementSettingsIdEndpoint import ProcurementSettingsIdEndpoint
from pywise.endpoints.ProcurementSettingsCountEndpoint import ProcurementSettingsCountEndpoint
from pywise.models.ProcurementSettingModel import ProcurementSettingModel

class ProcurementSettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "settings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementSettingsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementSettingsIdEndpoint:
        child = ProcurementSettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProcurementSettingModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProcurementSettingModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProcurementSettingModel]:
        return self._parse_many(ProcurementSettingModel, super().make_request("GET", params=params))
        