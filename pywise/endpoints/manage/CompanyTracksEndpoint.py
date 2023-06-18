from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyTracksIdEndpoint import CompanyTracksIdEndpoint
from pywise.endpoints.manage.CompanyTracksCountEndpoint import CompanyTracksCountEndpoint
from pywise.models.manage.TrackModel import TrackModel

class CompanyTracksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tracks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyTracksCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyTracksIdEndpoint:
        child = CompanyTracksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TrackModel]:
        """
        Performs a GET request against the /company/tracks endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TrackModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TrackModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TrackModel]:
        """
        Performs a GET request against the /company/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TrackModel]: The parsed response data.
        """
        return self._parse_many(TrackModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> TrackModel:
        """
        Performs a POST request against the /company/tracks endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TrackModel: The parsed response data.
        """
        return self._parse_one(TrackModel, super().make_request("POST", params=params).json())
        