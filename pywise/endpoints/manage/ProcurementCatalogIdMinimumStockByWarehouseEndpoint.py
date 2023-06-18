from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProcurementCatalogIdMinimumStockByWarehouseIdEndpoint import ProcurementCatalogIdMinimumStockByWarehouseIdEndpoint
from pywise.endpoints.manage.ProcurementCatalogIdMinimumStockByWarehouseCountEndpoint import ProcurementCatalogIdMinimumStockByWarehouseCountEndpoint
from pywise.models.manage.MinimumStockByWarehouseModel import MinimumStockByWarehouseModel

class ProcurementCatalogIdMinimumStockByWarehouseEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "minimumStockByWarehouse", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementCatalogIdMinimumStockByWarehouseCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementCatalogIdMinimumStockByWarehouseIdEndpoint:
        child = ProcurementCatalogIdMinimumStockByWarehouseIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MinimumStockByWarehouseModel]:
        """
        Performs a GET request against the /procurement/catalog/{parentId}/minimumStockByWarehouse endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MinimumStockByWarehouseModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MinimumStockByWarehouseModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MinimumStockByWarehouseModel]:
        """
        Performs a GET request against the /procurement/catalog/{parentId}/minimumStockByWarehouse endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MinimumStockByWarehouseModel]: The parsed response data.
        """
        return self._parse_many(MinimumStockByWarehouseModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MinimumStockByWarehouseModel:
        """
        Performs a POST request against the /procurement/catalog/{parentId}/minimumStockByWarehouse endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MinimumStockByWarehouseModel: The parsed response data.
        """
        return self._parse_one(MinimumStockByWarehouseModel, super().make_request("POST", params=params).json())
        