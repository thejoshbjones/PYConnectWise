from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SalesOpportunitiesIdForecastIdEndpoint import SalesOpportunitiesIdForecastIdEndpoint
from pywise.endpoints.manage.SalesOpportunitiesIdForecastCountEndpoint import SalesOpportunitiesIdForecastCountEndpoint
from pywise.models.manage.ForecastModel import ForecastModel

class SalesOpportunitiesIdForecastEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesIdForecastCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOpportunitiesIdForecastIdEndpoint:
        child = SalesOpportunitiesIdForecastIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ForecastModel:
        """
        Performs a PUT request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ForecastModel: The parsed response data.
        """
        return self._parse_one(ForecastModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ForecastModel:
        """
        Performs a PATCH request against the  endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ForecastModel: The parsed response data.
        """
        return self._parse_one(ForecastModel, super().make_request("PATCH", params=params).json())
        