from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemDocumentsIdEndpoint import SystemDocumentsIdEndpoint
from pywise.endpoints.SystemDocumentsCountEndpoint import SystemDocumentsCountEndpoint
from pywise.endpoints.SystemDocumentsUploadsampleEndpoint import SystemDocumentsUploadsampleEndpoint
from pywise.models.DocumentInfoModel import DocumentInfoModel

class SystemDocumentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "documents", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemDocumentsCountEndpoint(client, parent_endpoint=self)
        )
        self.uploadsample = self.register_child_endpoint(
            SystemDocumentsUploadsampleEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemDocumentsIdEndpoint:
        child = SystemDocumentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
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
    
    def get(self, data=None, params=None) -> list[DocumentInfoModel]:
        return self._parse_many(DocumentInfoModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> DocumentInfoModel:
        return self._parse_one(DocumentInfoModel, super().make_request("POST", params=params))
        