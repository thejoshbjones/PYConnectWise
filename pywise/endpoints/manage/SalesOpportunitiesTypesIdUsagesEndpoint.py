from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SalesOpportunitiesTypesIdUsagesListEndpoint import SalesOpportunitiesTypesIdUsagesListEndpoint
from pywise.models.manage.UsageModel import UsageModel

class SalesOpportunitiesTypesIdUsagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "usages", parent_endpoint=parent_endpoint)
        
        self.list = self.register_child_endpoint(
            SalesOpportunitiesTypesIdUsagesListEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[UsageModel]:
        """
        Performs a GET request against the /sales/opportunities/types/{id}/usages endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UsageModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            UsageModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[UsageModel]:
        """
        Performs a GET request against the /sales/opportunities/types/{id}/usages endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UsageModel]: The parsed response data.
        """
        return self._parse_many(UsageModel, super().make_request("GET", params=params).json())
        