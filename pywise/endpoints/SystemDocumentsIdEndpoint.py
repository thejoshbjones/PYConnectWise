from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemDocumentsIdDownloadEndpoint import SystemDocumentsIdDownloadEndpoint
from pywise.endpoints.SystemDocumentsIdThumbnailEndpoint import SystemDocumentsIdThumbnailEndpoint
from pywise.models.DocumentInfoModel import DocumentInfoModel

class SystemDocumentsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.download = self.register_child_endpoint(
            SystemDocumentsIdDownloadEndpoint(client, parent_endpoint=self)
        )
        self.thumbnail = self.register_child_endpoint(
            SystemDocumentsIdThumbnailEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[DocumentInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            DocumentInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> DocumentInfoModel:
        return self._parse_one(DocumentInfoModel, super().make_request("GET", params=params))
        
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def post(self, data=None, params=None) -> DocumentInfoModel:
        return self._parse_one(DocumentInfoModel, super().make_request("POST", params=params))
        