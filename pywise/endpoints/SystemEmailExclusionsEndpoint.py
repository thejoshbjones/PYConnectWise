from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemEmailExclusionsIdEndpoint import SystemEmailExclusionsIdEndpoint
from pywise.endpoints.SystemEmailExclusionsCountEndpoint import SystemEmailExclusionsCountEndpoint
from pywise.models.EmailExclusionModel import EmailExclusionModel

class SystemEmailExclusionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "emailExclusions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemEmailExclusionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemEmailExclusionsIdEndpoint:
        child = SystemEmailExclusionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[EmailExclusionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            EmailExclusionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[EmailExclusionModel]:
        return self._parse_many(EmailExclusionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> EmailExclusionModel:
        return self._parse_one(EmailExclusionModel, super().make_request("POST", params=params))
        