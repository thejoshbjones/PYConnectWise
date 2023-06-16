from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMycompanyDocumentsIdEndpoint import SystemMycompanyDocumentsIdEndpoint
from pywise.models.DocumentSetupModel import DocumentSetupModel

class SystemMycompanyDocumentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "documents", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> SystemMycompanyDocumentsIdEndpoint:
        child = SystemMycompanyDocumentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[DocumentSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            DocumentSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[DocumentSetupModel]:
        return self._parse_many(DocumentSetupModel, super().make_request("GET", params=params))
        