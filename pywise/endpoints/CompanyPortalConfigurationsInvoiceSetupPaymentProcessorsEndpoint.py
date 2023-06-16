from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsIdEndpoint import CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsIdEndpoint
from pywise.endpoints.CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsCountEndpoint import CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsCountEndpoint
from pywise.models.PortalConfigurationPaymentProcessorModel import PortalConfigurationPaymentProcessorModel

class CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "paymentProcessors", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsIdEndpoint:
        child = CompanyPortalConfigurationsInvoiceSetupPaymentProcessorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PortalConfigurationPaymentProcessorModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PortalConfigurationPaymentProcessorModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PortalConfigurationPaymentProcessorModel]:
        return self._parse_many(PortalConfigurationPaymentProcessorModel, super().make_request("GET", params=params))
        