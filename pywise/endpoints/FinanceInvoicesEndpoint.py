from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceInvoicesIdEndpoint import FinanceInvoicesIdEndpoint
from pywise.endpoints.FinanceInvoicesCountEndpoint import FinanceInvoicesCountEndpoint
from pywise.models.InvoiceModel import InvoiceModel

class FinanceInvoicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "invoices", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceInvoicesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceInvoicesIdEndpoint:
        child = FinanceInvoicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[InvoiceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            InvoiceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[InvoiceModel]:
        return self._parse_many(InvoiceModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> InvoiceModel:
        return self._parse_one(InvoiceModel, super().make_request("POST", params=params))
        