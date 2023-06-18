from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.FinanceAgreementsIdAdjustmentsIdEndpoint import FinanceAgreementsIdAdjustmentsIdEndpoint
from pywise.endpoints.manage.FinanceAgreementsIdAdjustmentsCountEndpoint import FinanceAgreementsIdAdjustmentsCountEndpoint
from pywise.models.manage.AdjustmentModel import AdjustmentModel

class FinanceAgreementsIdAdjustmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "adjustments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementsIdAdjustmentsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> FinanceAgreementsIdAdjustmentsIdEndpoint:
        child = FinanceAgreementsIdAdjustmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AdjustmentModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/adjustments endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AdjustmentModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AdjustmentModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AdjustmentModel]:
        """
        Performs a GET request against the /finance/agreements/{parentId}/adjustments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AdjustmentModel]: The parsed response data.
        """
        return self._parse_many(AdjustmentModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AdjustmentModel:
        """
        Performs a POST request against the /finance/agreements/{parentId}/adjustments endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AdjustmentModel: The parsed response data.
        """
        return self._parse_one(AdjustmentModel, super().make_request("POST", params=params).json())
        