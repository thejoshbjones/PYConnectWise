from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProcurementAdjustmentsIdDetailsIdEndpoint import ProcurementAdjustmentsIdDetailsIdEndpoint
from pywise.endpoints.manage.ProcurementAdjustmentsIdDetailsCountEndpoint import ProcurementAdjustmentsIdDetailsCountEndpoint
from pywise.models.manage.AdjustmentDetailModel import AdjustmentDetailModel

class ProcurementAdjustmentsIdDetailsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "details", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementAdjustmentsIdDetailsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementAdjustmentsIdDetailsIdEndpoint:
        child = ProcurementAdjustmentsIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AdjustmentDetailModel]:
        """
        Performs a GET request against the /procurement/adjustments/{parentId}/details endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AdjustmentDetailModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AdjustmentDetailModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AdjustmentDetailModel]:
        """
        Performs a GET request against the /procurement/adjustments/{parentId}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AdjustmentDetailModel]: The parsed response data.
        """
        return self._parse_many(AdjustmentDetailModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AdjustmentDetailModel:
        """
        Performs a POST request against the /procurement/adjustments/{parentId}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AdjustmentDetailModel: The parsed response data.
        """
        return self._parse_one(AdjustmentDetailModel, super().make_request("POST", params=params).json())
        