from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ExpenseClassificationsIdEndpoint import ExpenseClassificationsIdEndpoint
from pywise.endpoints.manage.ExpenseClassificationsCountEndpoint import ExpenseClassificationsCountEndpoint
from pywise.models.manage.ClassificationModel import ClassificationModel

class ExpenseClassificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "classifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ExpenseClassificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ExpenseClassificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ExpenseClassificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ExpenseClassificationsIdEndpoint: The initialized ExpenseClassificationsIdEndpoint object.
        """
        child = ExpenseClassificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ClassificationModel]:
        """
        Performs a GET request against the /expense/classifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ClassificationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ClassificationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ClassificationModel]:
        """
        Performs a GET request against the /expense/classifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ClassificationModel]: The parsed response data.
        """
        return self._parse_many(ClassificationModel, super().make_request("GET", params=params).json())
        