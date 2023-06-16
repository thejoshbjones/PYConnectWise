from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceTaxCodesIdExpenseTypeExemptionsIdEndpoint import FinanceTaxCodesIdExpenseTypeExemptionsIdEndpoint
from pywise.endpoints.FinanceTaxCodesIdExpenseTypeExemptionsCountEndpoint import FinanceTaxCodesIdExpenseTypeExemptionsCountEndpoint
from pywise.models.ExpenseTypeExemptionModel import ExpenseTypeExemptionModel

class FinanceTaxCodesIdExpenseTypeExemptionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "expenseTypeExemptions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxCodesIdExpenseTypeExemptionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceTaxCodesIdExpenseTypeExemptionsIdEndpoint:
        child = FinanceTaxCodesIdExpenseTypeExemptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ExpenseTypeExemptionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ExpenseTypeExemptionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ExpenseTypeExemptionModel]:
        return self._parse_many(ExpenseTypeExemptionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ExpenseTypeExemptionModel:
        return self._parse_one(ExpenseTypeExemptionModel, super().make_request("POST", params=params))
        