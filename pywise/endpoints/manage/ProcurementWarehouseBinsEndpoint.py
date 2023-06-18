from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProcurementWarehouseBinsIdEndpoint import ProcurementWarehouseBinsIdEndpoint
from pywise.endpoints.manage.ProcurementWarehouseBinsCountEndpoint import ProcurementWarehouseBinsCountEndpoint
from pywise.endpoints.manage.ProcurementWarehouseBinsInfoEndpoint import ProcurementWarehouseBinsInfoEndpoint
from pywise.models.manage.WarehouseBinModel import WarehouseBinModel

class ProcurementWarehouseBinsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "warehouseBins", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementWarehouseBinsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementWarehouseBinsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementWarehouseBinsIdEndpoint:
        child = ProcurementWarehouseBinsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WarehouseBinModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WarehouseBinModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WarehouseBinModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[WarehouseBinModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WarehouseBinModel]: The parsed response data.
        """
        return self._parse_many(WarehouseBinModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WarehouseBinModel:
        """
        Performs a POST request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WarehouseBinModel: The parsed response data.
        """
        return self._parse_one(WarehouseBinModel, super().make_request("POST", params=params).json())
        