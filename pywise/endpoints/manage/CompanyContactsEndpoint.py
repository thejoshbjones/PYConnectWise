from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyContactsIdEndpoint import CompanyContactsIdEndpoint
from pywise.endpoints.manage.CompanyContactsCountEndpoint import CompanyContactsCountEndpoint
from pywise.endpoints.manage.CompanyContactsDefaultEndpoint import CompanyContactsDefaultEndpoint
from pywise.endpoints.manage.CompanyContactsDepartmentsEndpoint import CompanyContactsDepartmentsEndpoint
from pywise.endpoints.manage.CompanyContactsRelationshipsEndpoint import CompanyContactsRelationshipsEndpoint
from pywise.endpoints.manage.CompanyContactsRequestPasswordEndpoint import CompanyContactsRequestPasswordEndpoint
from pywise.endpoints.manage.CompanyContactsTypesEndpoint import CompanyContactsTypesEndpoint
from pywise.endpoints.manage.CompanyContactsValidatePortalCredentialsEndpoint import CompanyContactsValidatePortalCredentialsEndpoint
from pywise.models.manage.ContactModel import ContactModel

class CompanyContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contacts", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            CompanyContactsDefaultEndpoint(client, parent_endpoint=self)
        )
        self.departments = self.register_child_endpoint(
            CompanyContactsDepartmentsEndpoint(client, parent_endpoint=self)
        )
        self.relationships = self.register_child_endpoint(
            CompanyContactsRelationshipsEndpoint(client, parent_endpoint=self)
        )
        self.requestPassword = self.register_child_endpoint(
            CompanyContactsRequestPasswordEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            CompanyContactsTypesEndpoint(client, parent_endpoint=self)
        )
        self.validatePortalCredentials = self.register_child_endpoint(
            CompanyContactsValidatePortalCredentialsEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyContactsIdEndpoint:
        child = CompanyContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ContactModel]:
        """
        Performs a GET request against the /company/contacts endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ContactModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[ContactModel]:
        """
        Performs a GET request against the /company/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactModel]: The parsed response data.
        """
        return self._parse_many(ContactModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ContactModel:
        """
        Performs a POST request against the /company/contacts endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactModel: The parsed response data.
        """
        return self._parse_one(ContactModel, super().make_request("POST", params=params).json())
        