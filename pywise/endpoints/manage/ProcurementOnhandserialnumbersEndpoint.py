from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProcurementOnhandserialnumbersIdEndpoint import ProcurementOnhandserialnumbersIdEndpoint
from pywise.endpoints.manage.ProcurementOnhandserialnumbersCountEndpoint import ProcurementOnhandserialnumbersCountEndpoint
from pywise.models.manage.OnHandSerialNumberModel import OnHandSerialNumberModel

class ProcurementOnhandserialnumbersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "onhandserialnumbers", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementOnhandserialnumbersCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementOnhandserialnumbersIdEndpoint:
        child = ProcurementOnhandserialnumbersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[OnHandSerialNumberModel]:
        """
        Performs a GET request against the  endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OnHandSerialNumberModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            OnHandSerialNumberModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OnHandSerialNumberModel]:
        """
        Performs a GET request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OnHandSerialNumberModel]: The parsed response data.
        """
        return self._parse_many(OnHandSerialNumberModel, super().make_request("GET", params=params).json())
        