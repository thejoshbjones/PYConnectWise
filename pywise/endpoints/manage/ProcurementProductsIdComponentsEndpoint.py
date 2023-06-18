from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProcurementProductsIdComponentsIdEndpoint import ProcurementProductsIdComponentsIdEndpoint
from pywise.endpoints.manage.ProcurementProductsIdComponentsCountEndpoint import ProcurementProductsIdComponentsCountEndpoint
from pywise.models.manage.ProductComponentModel import ProductComponentModel

class ProcurementProductsIdComponentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "components", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementProductsIdComponentsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementProductsIdComponentsIdEndpoint:
        child = ProcurementProductsIdComponentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProductComponentModel]:
        """
        Performs a GET request against the /procurement/products/{parentId}/components endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductComponentModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProductComponentModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductComponentModel]:
        """
        Performs a GET request against the /procurement/products/{parentId}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductComponentModel]: The parsed response data.
        """
        return self._parse_many(ProductComponentModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProductComponentModel]:
        """
        Performs a POST request against the /procurement/products/{parentId}/components endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductComponentModel]: The parsed response data.
        """
        return self._parse_many(ProductComponentModel, super().make_request("POST", params=params).json())
        