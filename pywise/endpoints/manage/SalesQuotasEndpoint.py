from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SalesQuotasIdEndpoint import SalesQuotasIdEndpoint
from pywise.endpoints.manage.SalesQuotasCountEndpoint import SalesQuotasCountEndpoint
from pywise.models.manage.SalesQuotaModel import SalesQuotaModel

class SalesQuotasEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "quotas", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesQuotasCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesQuotasIdEndpoint:
        child = SalesQuotasIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[SalesQuotaModel]:
        """
        Performs a GET request against the /sales/quotas endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SalesQuotaModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            SalesQuotaModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[SalesQuotaModel]:
        """
        Performs a GET request against the /sales/quotas endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SalesQuotaModel]: The parsed response data.
        """
        return self._parse_many(SalesQuotaModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> SalesQuotaModel:
        """
        Performs a POST request against the /sales/quotas endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SalesQuotaModel: The parsed response data.
        """
        return self._parse_one(SalesQuotaModel, super().make_request("POST", params=params).json())
        