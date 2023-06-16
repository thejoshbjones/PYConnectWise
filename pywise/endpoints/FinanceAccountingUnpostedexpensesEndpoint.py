from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingUnpostedexpensesIdEndpoint import FinanceAccountingUnpostedexpensesIdEndpoint
from pywise.endpoints.FinanceAccountingUnpostedexpensesCountEndpoint import FinanceAccountingUnpostedexpensesCountEndpoint
from pywise.models.UnpostedExpenseModel import UnpostedExpenseModel

class FinanceAccountingUnpostedexpensesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "unpostedexpenses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingUnpostedexpensesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAccountingUnpostedexpensesIdEndpoint:
        child = FinanceAccountingUnpostedexpensesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[UnpostedExpenseModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            UnpostedExpenseModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[UnpostedExpenseModel]:
        return self._parse_many(UnpostedExpenseModel, super().make_request("GET", params=params))
        