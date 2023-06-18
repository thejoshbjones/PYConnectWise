from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint import ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint
from pywise.endpoints.manage.ProcurementPricingschedulesIdDetailsIdBreaksCountEndpoint import ProcurementPricingschedulesIdDetailsIdBreaksCountEndpoint
from pywise.models.manage.PricingBreakModel import PricingBreakModel

class ProcurementPricingschedulesIdDetailsIdBreaksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "breaks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementPricingschedulesIdDetailsIdBreaksCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint:
        child = ProcurementPricingschedulesIdDetailsIdBreaksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PricingBreakModel]:
        """
        Performs a GET request against the /procurement/pricingschedules/{grandparentId}/details/{parentId}/breaks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PricingBreakModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PricingBreakModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PricingBreakModel]:
        """
        Performs a GET request against the /procurement/pricingschedules/{grandparentId}/details/{parentId}/breaks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PricingBreakModel]: The parsed response data.
        """
        return self._parse_many(PricingBreakModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PricingBreakModel:
        """
        Performs a POST request against the /procurement/pricingschedules/{grandparentId}/details/{parentId}/breaks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PricingBreakModel: The parsed response data.
        """
        return self._parse_one(PricingBreakModel, super().make_request("POST", params=params).json())
        