from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.models.manage.TicketModel import TicketModel

class SalesOrdersIdConvertToServiceTicketEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "convertToServiceTicket", parent_endpoint=parent_endpoint)
        
    
    
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TicketModel:
        """
        Performs a POST request against the /sales/orders/{id}/convertToServiceTicket endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TicketModel: The parsed response data.
        """
        return self._parse_one(TicketModel, super().make_request("POST", params=params).json())
        