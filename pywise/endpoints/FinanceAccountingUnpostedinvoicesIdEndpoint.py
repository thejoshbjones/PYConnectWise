from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingUnpostedinvoicesIdTaxableLevelsEndpoint import FinanceAccountingUnpostedinvoicesIdTaxableLevelsEndpoint
from pywise.models.UnpostedInvoiceModel import UnpostedInvoiceModel

class FinanceAccountingUnpostedinvoicesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.taxableLevels = self.register_child_endpoint(
            FinanceAccountingUnpostedinvoicesIdTaxableLevelsEndpoint(client, parent_endpoint=self)
        )
    
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
    
    def get(self, data=None, params=None) -> UnpostedInvoiceModel:
        return self._parse_one(UnpostedInvoiceModel, super().make_request("GET", params=params))
        