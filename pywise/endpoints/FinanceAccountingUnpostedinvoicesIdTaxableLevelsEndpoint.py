from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingUnpostedinvoicesIdTaxableLevelsIdEndpoint import FinanceAccountingUnpostedinvoicesIdTaxableLevelsIdEndpoint
from pywise.endpoints.FinanceAccountingUnpostedinvoicesIdTaxableLevelsCountEndpoint import FinanceAccountingUnpostedinvoicesIdTaxableLevelsCountEndpoint
from pywise.models.UnpostedInvoiceTaxableLevelModel import UnpostedInvoiceTaxableLevelModel

class FinanceAccountingUnpostedinvoicesIdTaxableLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingUnpostedinvoicesIdTaxableLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAccountingUnpostedinvoicesIdTaxableLevelsIdEndpoint:
        child = FinanceAccountingUnpostedinvoicesIdTaxableLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[UnpostedInvoiceTaxableLevelModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            UnpostedInvoiceTaxableLevelModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[UnpostedInvoiceTaxableLevelModel]:
        return self._parse_many(UnpostedInvoiceTaxableLevelModel, super().make_request("GET", params=params))
        