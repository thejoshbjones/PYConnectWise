from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyAddressFormatsIdEndpoint import CompanyAddressFormatsIdEndpoint
from pywise.endpoints.manage.CompanyAddressFormatsCountEndpoint import CompanyAddressFormatsCountEndpoint
from pywise.endpoints.manage.CompanyAddressFormatsInfoEndpoint import CompanyAddressFormatsInfoEndpoint
from pywise.models.manage.AddressFormatModel import AddressFormatModel

class CompanyAddressFormatsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "addressFormats", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyAddressFormatsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyAddressFormatsInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyAddressFormatsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyAddressFormatsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyAddressFormatsIdEndpoint: The initialized CompanyAddressFormatsIdEndpoint object.
        """
        child = CompanyAddressFormatsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AddressFormatModel]:
        """
        Performs a GET request against the /company/addressFormats endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AddressFormatModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AddressFormatModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AddressFormatModel]:
        """
        Performs a GET request against the /company/addressFormats endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AddressFormatModel]: The parsed response data.
        """
        return self._parse_many(AddressFormatModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AddressFormatModel:
        """
        Performs a POST request against the /company/addressFormats endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AddressFormatModel: The parsed response data.
        """
        return self._parse_one(AddressFormatModel, super().make_request("POST", params=params).json())
        