from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from typing import Any
from pywise.endpoints.manage.SystemFileuploadsettingsIdEndpoint import SystemFileuploadsettingsIdEndpoint
from pywise.endpoints.manage.SystemFileuploadsettingsCountEndpoint import SystemFileuploadsettingsCountEndpoint
from pywise.models.manage.FileUploadSettingModel import FileUploadSettingModel

class SystemFileuploadsettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemFileuploadsettingsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemFileuploadsettingsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemFileuploadsettingsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemFileuploadsettingsIdEndpoint: The initialized SystemFileuploadsettingsIdEndpoint object.
        """
        child = SystemFileuploadsettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[FileUploadSettingModel]:
        """
        Performs a GET request against the /system/fileuploadsettings/ endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[FileUploadSettingModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            FileUploadSettingModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[FileUploadSettingModel]:
        """
        Performs a GET request against the /system/fileuploadsettings/ endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[FileUploadSettingModel]: The parsed response data.
        """
        return self._parse_many(FileUploadSettingModel, super().make_request("GET", params=params).json())
        