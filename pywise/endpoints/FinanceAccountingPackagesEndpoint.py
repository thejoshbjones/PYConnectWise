from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingPackagesIdEndpoint import FinanceAccountingPackagesIdEndpoint
from pywise.endpoints.FinanceAccountingPackagesCountEndpoint import FinanceAccountingPackagesCountEndpoint
from pywise.models.AccountingPackageModel import AccountingPackageModel

class FinanceAccountingPackagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "accountingPackages", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingPackagesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAccountingPackagesIdEndpoint:
        child = FinanceAccountingPackagesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AccountingPackageModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AccountingPackageModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AccountingPackageModel]:
        return self._parse_many(AccountingPackageModel, super().make_request("GET", params=params))
        