from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceCodesIdEndpoint import ServiceCodesIdEndpoint
from pywise.endpoints.ServiceCodesCountEndpoint import ServiceCodesCountEndpoint
from pywise.models.CodeModel import CodeModel

class ServiceCodesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "codes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceCodesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceCodesIdEndpoint:
        child = ServiceCodesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CodeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CodeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CodeModel]:
        return self._parse_many(CodeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CodeModel:
        return self._parse_one(CodeModel, super().make_request("POST", params=params))
        