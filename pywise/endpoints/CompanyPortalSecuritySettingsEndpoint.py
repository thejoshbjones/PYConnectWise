from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyPortalSecuritySettingsIdEndpoint import CompanyPortalSecuritySettingsIdEndpoint
from pywise.endpoints.CompanyPortalSecuritySettingsCountEndpoint import CompanyPortalSecuritySettingsCountEndpoint
from pywise.models.PortalSecuritySettingModel import PortalSecuritySettingModel

class CompanyPortalSecuritySettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "portalSecuritySettings", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyPortalSecuritySettingsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyPortalSecuritySettingsIdEndpoint:
        child = CompanyPortalSecuritySettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PortalSecuritySettingModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PortalSecuritySettingModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PortalSecuritySettingModel]:
        return self._parse_many(PortalSecuritySettingModel, super().make_request("GET", params=params))
        