from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceInvoiceTemplatesIdEndpoint import FinanceInvoiceTemplatesIdEndpoint
from pywise.endpoints.FinanceInvoiceTemplatesCountEndpoint import FinanceInvoiceTemplatesCountEndpoint
from pywise.models.InvoiceTemplateModel import InvoiceTemplateModel

class FinanceInvoiceTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoiceTemplates", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceInvoiceTemplatesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceInvoiceTemplatesIdEndpoint:
        child = FinanceInvoiceTemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[InvoiceTemplateModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            InvoiceTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[InvoiceTemplateModel]:
        return self._parse_many(InvoiceTemplateModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> InvoiceTemplateModel:
        return self._parse_one(InvoiceTemplateModel, super().make_request("POST", params=params))
        