from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProcurementAdjustmentsIdEndpoint import ProcurementAdjustmentsIdEndpoint
from pywise.endpoints.manage.ProcurementAdjustmentsCountEndpoint import ProcurementAdjustmentsCountEndpoint
from pywise.endpoints.manage.ProcurementAdjustmentsTypesEndpoint import ProcurementAdjustmentsTypesEndpoint
from pywise.models.manage.ProcurementAdjustmentModel import ProcurementAdjustmentModel

class ProcurementAdjustmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "adjustments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementAdjustmentsCountEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            ProcurementAdjustmentsTypesEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementAdjustmentsIdEndpoint:
        child = ProcurementAdjustmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ProcurementAdjustmentModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProcurementAdjustmentModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ProcurementAdjustmentModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ProcurementAdjustmentModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProcurementAdjustmentModel]: The parsed response data.
        """
        return self._parse_many(ProcurementAdjustmentModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ProcurementAdjustmentModel:
        """
        Performs a POST request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProcurementAdjustmentModel: The parsed response data.
        """
        return self._parse_one(ProcurementAdjustmentModel, super().make_request("POST", params=params).json())
        