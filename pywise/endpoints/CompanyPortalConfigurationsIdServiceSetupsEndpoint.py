from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyPortalConfigurationsIdServiceSetupsIdEndpoint import CompanyPortalConfigurationsIdServiceSetupsIdEndpoint
from pywise.endpoints.CompanyPortalConfigurationsIdServiceSetupsCountEndpoint import CompanyPortalConfigurationsIdServiceSetupsCountEndpoint
from pywise.models.PortalConfigurationServiceSetupModel import PortalConfigurationServiceSetupModel

class CompanyPortalConfigurationsIdServiceSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "serviceSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyPortalConfigurationsIdServiceSetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyPortalConfigurationsIdServiceSetupsIdEndpoint:
        child = CompanyPortalConfigurationsIdServiceSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PortalConfigurationServiceSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PortalConfigurationServiceSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PortalConfigurationServiceSetupModel]:
        return self._parse_many(PortalConfigurationServiceSetupModel, super().make_request("GET", params=params))
        