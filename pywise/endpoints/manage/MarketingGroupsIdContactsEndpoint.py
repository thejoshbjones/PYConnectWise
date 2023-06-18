from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.MarketingGroupsIdContactsIdEndpoint import MarketingGroupsIdContactsIdEndpoint
from pywise.endpoints.manage.MarketingGroupsIdContactsCountEndpoint import MarketingGroupsIdContactsCountEndpoint
from pywise.models.manage.MarketingContactModel import MarketingContactModel

class MarketingGroupsIdContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contacts", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            MarketingGroupsIdContactsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> MarketingGroupsIdContactsIdEndpoint:
        child = MarketingGroupsIdContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MarketingContactModel]:
        """
        Performs a GET request against the /marketing/groups/{parentId}/contacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MarketingContactModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MarketingContactModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MarketingContactModel]:
        """
        Performs a GET request against the /marketing/groups/{parentId}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MarketingContactModel]: The parsed response data.
        """
        return self._parse_many(MarketingContactModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MarketingContactModel:
        """
        Performs a POST request against the /marketing/groups/{parentId}/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MarketingContactModel: The parsed response data.
        """
        return self._parse_one(MarketingContactModel, super().make_request("POST", params=params).json())
        