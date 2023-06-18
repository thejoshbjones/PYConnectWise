from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.models.manage.LocationDepartmentModel import LocationDepartmentModel

class SystemLocationsIdDepartmentsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[LocationDepartmentModel]:
        """
        Performs a GET request against the /system/locations/{parentId}/departments/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LocationDepartmentModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            LocationDepartmentModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LocationDepartmentModel:
        """
        Performs a GET request against the /system/locations/{parentId}/departments/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LocationDepartmentModel: The parsed response data.
        """
        return self._parse_one(LocationDepartmentModel, super().make_request("GET", params=params).json())
        