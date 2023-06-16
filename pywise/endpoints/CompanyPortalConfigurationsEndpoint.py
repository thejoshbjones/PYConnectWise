from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyPortalConfigurationsIdEndpoint import CompanyPortalConfigurationsIdEndpoint
from pywise.endpoints.CompanyPortalConfigurationsCopyEndpoint import CompanyPortalConfigurationsCopyEndpoint
from pywise.endpoints.CompanyPortalConfigurationsCountEndpoint import CompanyPortalConfigurationsCountEndpoint
from pywise.models.PortalConfigurationModel import PortalConfigurationModel

class CompanyPortalConfigurationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "portalConfigurations", parent_endpoint=parent_endpoint)
        
        self.copy = self.register_child_endpoint(
            CompanyPortalConfigurationsCopyEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            CompanyPortalConfigurationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyPortalConfigurationsIdEndpoint:
        child = CompanyPortalConfigurationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PortalConfigurationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PortalConfigurationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PortalConfigurationModel]:
        return self._parse_many(PortalConfigurationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> PortalConfigurationModel:
        return self._parse_one(PortalConfigurationModel, super().make_request("POST", params=params))
        