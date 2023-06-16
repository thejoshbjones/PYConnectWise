from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingBatchesIdEndpoint import FinanceAccountingBatchesIdEndpoint
from pywise.endpoints.FinanceAccountingBatchesCountEndpoint import FinanceAccountingBatchesCountEndpoint
from pywise.models.AccountingBatchModel import AccountingBatchModel
from pywise.models.GLExportModel import GLExportModel

class FinanceAccountingBatchesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "batches", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingBatchesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAccountingBatchesIdEndpoint:
        child = FinanceAccountingBatchesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[GLExportModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            GLExportModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AccountingBatchModel]:
        return self._parse_many(AccountingBatchModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> GLExportModel:
        return self._parse_one(GLExportModel, super().make_request("POST", params=params))
        