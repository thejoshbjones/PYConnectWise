from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.ProcurementRmaTagsIdEndpoint import ProcurementRmaTagsIdEndpoint
from pywise.endpoints.manage.ProcurementRmaTagsCountEndpoint import ProcurementRmaTagsCountEndpoint
from pywise.endpoints.manage.ProcurementRmaTagsDefaultEndpoint import ProcurementRmaTagsDefaultEndpoint
from pywise.models.manage.RmaTagModel import RmaTagModel

class ProcurementRmaTagsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "rmaTags", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementRmaTagsCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            ProcurementRmaTagsDefaultEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProcurementRmaTagsIdEndpoint:
        child = ProcurementRmaTagsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[RmaTagModel]:
        """
        Performs a GET request against the /procurement/rmaTags endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[RmaTagModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            RmaTagModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[RmaTagModel]:
        """
        Performs a GET request against the /procurement/rmaTags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[RmaTagModel]: The parsed response data.
        """
        return self._parse_many(RmaTagModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> RmaTagModel:
        """
        Performs a POST request against the /procurement/rmaTags endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            RmaTagModel: The parsed response data.
        """
        return self._parse_one(RmaTagModel, super().make_request("POST", params=params).json())
        