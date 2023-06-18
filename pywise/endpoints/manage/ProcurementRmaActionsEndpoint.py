from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProcurementRmaActionsIdEndpoint import ProcurementRmaActionsIdEndpoint
from pywise.endpoints.manage.ProcurementRmaActionsCountEndpoint import ProcurementRmaActionsCountEndpoint
from pywise.endpoints.manage.ProcurementRmaActionsInfoEndpoint import ProcurementRmaActionsInfoEndpoint
from pywise.models.manage.RmaActionModel import RmaActionModel

class ProcurementRmaActionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "rmaActions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementRmaActionsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProcurementRmaActionsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementRmaActionsIdEndpoint:
        child = ProcurementRmaActionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[RmaActionModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaActionModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            RmaActionModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RmaActionModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaActionModel]: The parsed response data.
        """
        return self._parse_many(RmaActionModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaActionModel:
        """
        Performs a POST request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaActionModel: The parsed response data.
        """
        return self._parse_one(RmaActionModel, super().make_request("POST", params=params).json())
        