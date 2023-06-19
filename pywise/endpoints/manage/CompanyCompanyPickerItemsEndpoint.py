from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyCompanyPickerItemsIdEndpoint import CompanyCompanyPickerItemsIdEndpoint
from pywise.endpoints.manage.CompanyCompanyPickerItemsClearEndpoint import CompanyCompanyPickerItemsClearEndpoint
from pywise.endpoints.manage.CompanyCompanyPickerItemsCountEndpoint import CompanyCompanyPickerItemsCountEndpoint
from pywise.models.manage.CompanyPickerItemModel import CompanyPickerItemModel

class CompanyCompanyPickerItemsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companyPickerItems", parent_endpoint=parent_endpoint)
        
        self.clear = self.register_child_endpoint(
            CompanyCompanyPickerItemsClearEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            CompanyCompanyPickerItemsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> CompanyCompanyPickerItemsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCompanyPickerItemsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCompanyPickerItemsIdEndpoint: The initialized CompanyCompanyPickerItemsIdEndpoint object.
        """
        child = CompanyCompanyPickerItemsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyPickerItemModel]:
        """
        Performs a GET request against the /company/companyPickerItems endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyPickerItemModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyPickerItemModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyPickerItemModel]:
        """
        Performs a GET request against the /company/companyPickerItems endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyPickerItemModel]: The parsed response data.
        """
        return self._parse_many(CompanyPickerItemModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyPickerItemModel:
        """
        Performs a POST request against the /company/companyPickerItems endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyPickerItemModel: The parsed response data.
        """
        return self._parse_one(CompanyPickerItemModel, super().make_request("POST", params=params).json())
        