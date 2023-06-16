from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceInvoiceEmailTemplatesIdEndpoint import FinanceInvoiceEmailTemplatesIdEndpoint
from pywise.endpoints.FinanceInvoiceEmailTemplatesCountEndpoint import FinanceInvoiceEmailTemplatesCountEndpoint
from pywise.endpoints.FinanceInvoiceEmailTemplatesInfoEndpoint import FinanceInvoiceEmailTemplatesInfoEndpoint
from pywise.models.InvoiceEmailTemplateModel import InvoiceEmailTemplateModel

class FinanceInvoiceEmailTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoiceEmailTemplates", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceInvoiceEmailTemplatesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceInvoiceEmailTemplatesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceInvoiceEmailTemplatesIdEndpoint:
        child = FinanceInvoiceEmailTemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[InvoiceEmailTemplateModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            InvoiceEmailTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[InvoiceEmailTemplateModel]:
        return self._parse_many(InvoiceEmailTemplateModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> InvoiceEmailTemplateModel:
        return self._parse_one(InvoiceEmailTemplateModel, super().make_request("POST", params=params))
        