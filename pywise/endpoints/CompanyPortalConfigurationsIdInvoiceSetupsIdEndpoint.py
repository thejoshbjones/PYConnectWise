from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyPortalConfigurationsIdInvoiceSetupsIdTestTransactionEndpoint import CompanyPortalConfigurationsIdInvoiceSetupsIdTestTransactionEndpoint
from pywise.models.PortalConfigurationInvoiceSetupModel import PortalConfigurationInvoiceSetupModel

class CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.testTransaction = self.register_child_endpoint(
            CompanyPortalConfigurationsIdInvoiceSetupsIdTestTransactionEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PortalConfigurationInvoiceSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PortalConfigurationInvoiceSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> PortalConfigurationInvoiceSetupModel:
        return self._parse_one(PortalConfigurationInvoiceSetupModel, super().make_request("GET", params=params))
        
    def put(self, data=None, params=None) -> PortalConfigurationInvoiceSetupModel:
        return self._parse_one(PortalConfigurationInvoiceSetupModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> PortalConfigurationInvoiceSetupModel:
        return self._parse_one(PortalConfigurationInvoiceSetupModel, super().make_request("PATCH", params=params))
        