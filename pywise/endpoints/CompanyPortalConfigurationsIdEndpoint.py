from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyPortalConfigurationsIdInvoiceSetupsEndpoint import CompanyPortalConfigurationsIdInvoiceSetupsEndpoint
from pywise.endpoints.CompanyPortalConfigurationsIdOpportunitySetupsEndpoint import CompanyPortalConfigurationsIdOpportunitySetupsEndpoint
from pywise.endpoints.CompanyPortalConfigurationsIdPasswordEmailSetupsEndpoint import CompanyPortalConfigurationsIdPasswordEmailSetupsEndpoint
from pywise.endpoints.CompanyPortalConfigurationsIdProjectSetupsEndpoint import CompanyPortalConfigurationsIdProjectSetupsEndpoint
from pywise.endpoints.CompanyPortalConfigurationsIdServiceSetupsEndpoint import CompanyPortalConfigurationsIdServiceSetupsEndpoint
from pywise.models.PortalConfigurationModel import PortalConfigurationModel

class CompanyPortalConfigurationsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.invoiceSetups = self.register_child_endpoint(
            CompanyPortalConfigurationsIdInvoiceSetupsEndpoint(client, parent_endpoint=self)
        )
        self.opportunitySetups = self.register_child_endpoint(
            CompanyPortalConfigurationsIdOpportunitySetupsEndpoint(client, parent_endpoint=self)
        )
        self.passwordEmailSetups = self.register_child_endpoint(
            CompanyPortalConfigurationsIdPasswordEmailSetupsEndpoint(client, parent_endpoint=self)
        )
        self.projectSetups = self.register_child_endpoint(
            CompanyPortalConfigurationsIdProjectSetupsEndpoint(client, parent_endpoint=self)
        )
        self.serviceSetups = self.register_child_endpoint(
            CompanyPortalConfigurationsIdServiceSetupsEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> PortalConfigurationModel:
        return self._parse_one(PortalConfigurationModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> PortalConfigurationModel:
        return self._parse_one(PortalConfigurationModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> PortalConfigurationModel:
        return self._parse_one(PortalConfigurationModel, super().make_request("PATCH", params=params))
        