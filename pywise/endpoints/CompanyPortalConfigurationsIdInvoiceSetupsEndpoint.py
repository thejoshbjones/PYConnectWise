from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint import CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint
from pywise.endpoints.CompanyPortalConfigurationsIdInvoiceSetupsCountEndpoint import CompanyPortalConfigurationsIdInvoiceSetupsCountEndpoint
from pywise.models.PortalConfigurationInvoiceSetupModel import PortalConfigurationInvoiceSetupModel

class CompanyPortalConfigurationsIdInvoiceSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoiceSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyPortalConfigurationsIdInvoiceSetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint:
        child = CompanyPortalConfigurationsIdInvoiceSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
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
    
    def get(self, data=None, params=None) -> list[PortalConfigurationInvoiceSetupModel]:
        return self._parse_many(PortalConfigurationInvoiceSetupModel, super().make_request("GET", params=params))
        