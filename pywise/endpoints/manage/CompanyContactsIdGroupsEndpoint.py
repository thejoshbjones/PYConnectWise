from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyContactsIdGroupsIdEndpoint import CompanyContactsIdGroupsIdEndpoint
from pywise.endpoints.manage.CompanyContactsIdGroupsCountEndpoint import CompanyContactsIdGroupsCountEndpoint
from pywise.models.manage.ContactGroupModel import ContactGroupModel

class CompanyContactsIdGroupsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "groups", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsIdGroupsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyContactsIdGroupsIdEndpoint:
        child = CompanyContactsIdGroupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ContactGroupModel]:
        """
        Performs a GET request against the /company/contacts/{parentId}/groups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactGroupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ContactGroupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactGroupModel]:
        """
        Performs a GET request against the /company/contacts/{parentId}/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactGroupModel]: The parsed response data.
        """
        return self._parse_many(ContactGroupModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactGroupModel:
        """
        Performs a POST request against the /company/contacts/{parentId}/groups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactGroupModel: The parsed response data.
        """
        return self._parse_one(ContactGroupModel, super().make_request("POST", params=params).json())
        