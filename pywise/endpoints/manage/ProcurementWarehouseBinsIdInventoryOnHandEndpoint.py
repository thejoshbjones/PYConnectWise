from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProcurementWarehouseBinsIdInventoryOnHandIdEndpoint import ProcurementWarehouseBinsIdInventoryOnHandIdEndpoint
from pywise.endpoints.manage.ProcurementWarehouseBinsIdInventoryOnHandCountEndpoint import ProcurementWarehouseBinsIdInventoryOnHandCountEndpoint
from pywise.models.manage.InventoryOnHandModel import InventoryOnHandModel

class ProcurementWarehouseBinsIdInventoryOnHandEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "inventoryOnHand", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementWarehouseBinsIdInventoryOnHandCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementWarehouseBinsIdInventoryOnHandIdEndpoint:
        child = ProcurementWarehouseBinsIdInventoryOnHandIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[InventoryOnHandModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[InventoryOnHandModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            InventoryOnHandModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[InventoryOnHandModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[InventoryOnHandModel]: The parsed response data.
        """
        return self._parse_many(InventoryOnHandModel, super().make_request("GET", params=params).json())
        