from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTicketsIdDocumentsCountEndpoint import ServiceTicketsIdDocumentsCountEndpoint
from pywise.models.DocumentReferenceModel import DocumentReferenceModel

class ServiceTicketsIdDocumentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "documents", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketsIdDocumentsCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[DocumentReferenceModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            DocumentReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[DocumentReferenceModel]:
        return self._parse_many(DocumentReferenceModel, super().make_request("GET", params=params))
        