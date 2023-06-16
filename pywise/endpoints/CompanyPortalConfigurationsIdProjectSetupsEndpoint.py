from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyPortalConfigurationsIdProjectSetupsIdEndpoint import CompanyPortalConfigurationsIdProjectSetupsIdEndpoint
from pywise.endpoints.CompanyPortalConfigurationsIdProjectSetupsCountEndpoint import CompanyPortalConfigurationsIdProjectSetupsCountEndpoint
from pywise.models.PortalConfigurationProjectSetupModel import PortalConfigurationProjectSetupModel

class CompanyPortalConfigurationsIdProjectSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "projectSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyPortalConfigurationsIdProjectSetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyPortalConfigurationsIdProjectSetupsIdEndpoint:
        child = CompanyPortalConfigurationsIdProjectSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PortalConfigurationProjectSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PortalConfigurationProjectSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PortalConfigurationProjectSetupModel]:
        return self._parse_many(PortalConfigurationProjectSetupModel, super().make_request("GET", params=params))
        