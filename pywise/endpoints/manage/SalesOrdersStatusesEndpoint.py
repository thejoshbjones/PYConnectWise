from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SalesOrdersStatusesIdEndpoint import SalesOrdersStatusesIdEndpoint
from pywise.endpoints.manage.SalesOrdersStatusesCountEndpoint import SalesOrdersStatusesCountEndpoint
from pywise.endpoints.manage.SalesOrdersStatusesInfoEndpoint import SalesOrdersStatusesInfoEndpoint
from pywise.models.manage.OrderStatusModel import OrderStatusModel

class SalesOrdersStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOrdersStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            SalesOrdersStatusesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOrdersStatusesIdEndpoint:
        child = SalesOrdersStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OrderStatusModel]:
        """
        Performs a GET request against the /sales/orders/statuses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OrderStatusModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OrderStatusModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OrderStatusModel]:
        """
        Performs a GET request against the /sales/orders/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OrderStatusModel]: The parsed response data.
        """
        return self._parse_many(OrderStatusModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OrderStatusModel]:
        """
        Performs a POST request against the /sales/orders/statuses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OrderStatusModel]: The parsed response data.
        """
        return self._parse_many(OrderStatusModel, super().make_request("POST", params=params).json())
        