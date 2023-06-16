from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyPortalConfigurationsIdPasswordEmailSetupsIdEndpoint import CompanyPortalConfigurationsIdPasswordEmailSetupsIdEndpoint
from pywise.models.PortalConfigurationPasswordEmailSetupModel import PortalConfigurationPasswordEmailSetupModel

class CompanyPortalConfigurationsIdPasswordEmailSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "passwordEmailSetups", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> CompanyPortalConfigurationsIdPasswordEmailSetupsIdEndpoint:
        child = CompanyPortalConfigurationsIdPasswordEmailSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PortalConfigurationPasswordEmailSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PortalConfigurationPasswordEmailSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PortalConfigurationPasswordEmailSetupModel]:
        return self._parse_many(PortalConfigurationPasswordEmailSetupModel, super().make_request("GET", params=params))
        