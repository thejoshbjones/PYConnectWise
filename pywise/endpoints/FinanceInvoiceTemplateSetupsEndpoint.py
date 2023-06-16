from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceInvoiceTemplateSetupsIdEndpoint import FinanceInvoiceTemplateSetupsIdEndpoint
from pywise.endpoints.FinanceInvoiceTemplateSetupsCountEndpoint import FinanceInvoiceTemplateSetupsCountEndpoint
from pywise.models.InvoiceTemplateSetupModel import InvoiceTemplateSetupModel

class FinanceInvoiceTemplateSetupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoiceTemplateSetups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceInvoiceTemplateSetupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceInvoiceTemplateSetupsIdEndpoint:
        child = FinanceInvoiceTemplateSetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[InvoiceTemplateSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            InvoiceTemplateSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[InvoiceTemplateSetupModel]:
        return self._parse_many(InvoiceTemplateSetupModel, super().make_request("GET", params=params))
        