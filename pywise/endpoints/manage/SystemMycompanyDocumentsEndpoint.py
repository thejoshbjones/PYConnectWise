from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemMycompanyDocumentsIdEndpoint import SystemMycompanyDocumentsIdEndpoint
from pywise.models.manage.DocumentSetupModel import DocumentSetupModel

class SystemMycompanyDocumentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "documents", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> SystemMycompanyDocumentsIdEndpoint:
        child = SystemMycompanyDocumentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[DocumentSetupModel]:
        """
        Performs a GET request against the /system/mycompany/documents endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[DocumentSetupModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            DocumentSetupModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[DocumentSetupModel]:
        """
        Performs a GET request against the /system/mycompany/documents endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[DocumentSetupModel]: The parsed response data.
        """
        return self._parse_many(DocumentSetupModel, super().make_request("GET", params=params).json())
        