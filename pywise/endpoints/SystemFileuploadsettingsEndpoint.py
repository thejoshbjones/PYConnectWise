from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemFileuploadsettingsIdEndpoint import SystemFileuploadsettingsIdEndpoint
from pywise.endpoints.SystemFileuploadsettingsCountEndpoint import SystemFileuploadsettingsCountEndpoint
from pywise.models.FileUploadSettingModel import FileUploadSettingModel

class SystemFileuploadsettingsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemFileuploadsettingsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemFileuploadsettingsIdEndpoint:
        child = SystemFileuploadsettingsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[FileUploadSettingModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            FileUploadSettingModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[FileUploadSettingModel]:
        return self._parse_many(FileUploadSettingModel, super().make_request("GET", params=params))
        