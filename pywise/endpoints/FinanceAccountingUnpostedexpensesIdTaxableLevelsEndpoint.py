from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint import FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint
from pywise.endpoints.FinanceAccountingUnpostedexpensesIdTaxableLevelsCountEndpoint import FinanceAccountingUnpostedexpensesIdTaxableLevelsCountEndpoint
from pywise.models.UnpostedExpenseTaxableLevelModel import UnpostedExpenseTaxableLevelModel

class FinanceAccountingUnpostedexpensesIdTaxableLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxableLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingUnpostedexpensesIdTaxableLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint:
        child = FinanceAccountingUnpostedexpensesIdTaxableLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[UnpostedExpenseTaxableLevelModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            UnpostedExpenseTaxableLevelModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[UnpostedExpenseTaxableLevelModel]:
        return self._parse_many(UnpostedExpenseTaxableLevelModel, super().make_request("GET", params=params))
        