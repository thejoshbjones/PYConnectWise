from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.CompanyCompaniesIdCustomStatusNotesIdEndpoint import CompanyCompaniesIdCustomStatusNotesIdEndpoint
from pywise.endpoints.manage.CompanyCompaniesIdCustomStatusNotesCountEndpoint import CompanyCompaniesIdCustomStatusNotesCountEndpoint
from pywise.models.manage.CompanyCustomNoteModel import CompanyCustomNoteModel

class CompanyCompaniesIdCustomStatusNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "customStatusNotes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdCustomStatusNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdCustomStatusNotesIdEndpoint:
        child = CompanyCompaniesIdCustomStatusNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyCustomNoteModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/customStatusNotes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyCustomNoteModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyCustomNoteModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CompanyCustomNoteModel]:
        """
        Performs a GET request against the /company/companies/{parentId}/customStatusNotes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CompanyCustomNoteModel]: The parsed response data.
        """
        return self._parse_many(CompanyCustomNoteModel, super().make_request("GET", params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyCustomNoteModel:
        """
        Performs a POST request against the /company/companies/{parentId}/customStatusNotes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyCustomNoteModel: The parsed response data.
        """
        return self._parse_one(CompanyCustomNoteModel, super().make_request("POST", params=params).json())
        