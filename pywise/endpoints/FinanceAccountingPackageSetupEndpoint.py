from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceAccountingPackageSetupIdEndpoint import FinanceAccountingPackageSetupIdEndpoint
from pywise.endpoints.FinanceAccountingPackageSetupCountEndpoint import FinanceAccountingPackageSetupCountEndpoint
from pywise.models.AccountingPackageSetupModel import AccountingPackageSetupModel

class FinanceAccountingPackageSetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "accountingPackageSetup", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingPackageSetupCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAccountingPackageSetupIdEndpoint:
        child = FinanceAccountingPackageSetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AccountingPackageSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AccountingPackageSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AccountingPackageSetupModel]:
        return self._parse_many(AccountingPackageSetupModel, super().make_request("GET", params=params))
        