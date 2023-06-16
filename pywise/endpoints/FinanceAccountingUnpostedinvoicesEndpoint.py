from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingUnpostedinvoicesIdEndpoint import FinanceAccountingUnpostedinvoicesIdEndpoint
from pywise.endpoints.FinanceAccountingUnpostedinvoicesCountEndpoint import FinanceAccountingUnpostedinvoicesCountEndpoint
from pywise.models.UnpostedInvoiceModel import UnpostedInvoiceModel

class FinanceAccountingUnpostedinvoicesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "unpostedinvoices", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingUnpostedinvoicesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAccountingUnpostedinvoicesIdEndpoint:
        child = FinanceAccountingUnpostedinvoicesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[UnpostedInvoiceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            UnpostedInvoiceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[UnpostedInvoiceModel]:
        return self._parse_many(UnpostedInvoiceModel, super().make_request("GET", params=params))
        