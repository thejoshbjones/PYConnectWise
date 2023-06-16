from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceInvoiceTemplatesIdUsagesEndpoint import FinanceInvoiceTemplatesIdUsagesEndpoint
from pywise.models.InvoiceTemplateModel import InvoiceTemplateModel

class FinanceInvoiceTemplatesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.usages = self.register_child_endpoint(
            FinanceInvoiceTemplatesIdUsagesEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> InvoiceTemplateModel:
        return self._parse_one(InvoiceTemplateModel, super().make_request("GET", params=params))
        
    def patch(self, data=None, params=None) -> InvoiceTemplateModel:
        return self._parse_one(InvoiceTemplateModel, super().make_request("PATCH", params=params))
        
    def put(self, data=None, params=None) -> InvoiceTemplateModel:
        return self._parse_one(InvoiceTemplateModel, super().make_request("PUT", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        