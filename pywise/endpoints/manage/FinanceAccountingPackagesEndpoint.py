from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.FinanceAccountingPackagesIdEndpoint import FinanceAccountingPackagesIdEndpoint
from pywise.endpoints.manage.FinanceAccountingPackagesCountEndpoint import FinanceAccountingPackagesCountEndpoint
from pywise.models.manage.AccountingPackageModel import AccountingPackageModel

class FinanceAccountingPackagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "accountingPackages", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAccountingPackagesCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAccountingPackagesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingPackagesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingPackagesIdEndpoint: The initialized FinanceAccountingPackagesIdEndpoint object.
        """
        child = FinanceAccountingPackagesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AccountingPackageModel]:
        """
        Performs a GET request against the /finance/accountingPackages endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AccountingPackageModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AccountingPackageModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AccountingPackageModel]:
        """
        Performs a GET request against the /finance/accountingPackages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AccountingPackageModel]: The parsed response data.
        """
        return self._parse_many(AccountingPackageModel, super().make_request("GET", params=params).json())
        