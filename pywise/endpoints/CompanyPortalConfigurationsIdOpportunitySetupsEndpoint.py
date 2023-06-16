from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyPortalConfigurationsIdOpportunitySetupsIdEndpoint import CompanyPortalConfigurationsIdOpportunitySetupsIdEndpoint
from pywise.models.PortalConfigurationOpportunitySetupModel import PortalConfigurationOpportunitySetupModel

class CompanyPortalConfigurationsIdOpportunitySetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "opportunitySetups", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> CompanyPortalConfigurationsIdOpportunitySetupsIdEndpoint:
        child = CompanyPortalConfigurationsIdOpportunitySetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PortalConfigurationOpportunitySetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PortalConfigurationOpportunitySetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PortalConfigurationOpportunitySetupModel]:
        return self._parse_many(PortalConfigurationOpportunitySetupModel, super().make_request("GET", params=params))
        
    def put(self, data=None, params=None) -> PortalConfigurationOpportunitySetupModel:
        return self._parse_one(PortalConfigurationOpportunitySetupModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> PortalConfigurationOpportunitySetupModel:
        return self._parse_one(PortalConfigurationOpportunitySetupModel, super().make_request("PATCH", params=params))
        