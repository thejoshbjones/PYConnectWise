from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyContactsRelationshipsIdEndpoint import CompanyContactsRelationshipsIdEndpoint
from pywise.endpoints.manage.CompanyContactsRelationshipsCountEndpoint import CompanyContactsRelationshipsCountEndpoint
from pywise.models.manage.ContactRelationshipModel import ContactRelationshipModel

class CompanyContactsRelationshipsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "relationships", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsRelationshipsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyContactsRelationshipsIdEndpoint:
        child = CompanyContactsRelationshipsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ContactRelationshipModel]:
        """
        Performs a GET request against the /company/contacts/relationships endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactRelationshipModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ContactRelationshipModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactRelationshipModel]:
        """
        Performs a GET request against the /company/contacts/relationships endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactRelationshipModel]: The parsed response data.
        """
        return self._parse_many(ContactRelationshipModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactRelationshipModel:
        """
        Performs a POST request against the /company/contacts/relationships endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactRelationshipModel: The parsed response data.
        """
        return self._parse_one(ContactRelationshipModel, super().make_request("POST", params=params).json())
        