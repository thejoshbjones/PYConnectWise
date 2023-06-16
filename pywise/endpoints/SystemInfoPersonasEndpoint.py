from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemInfoPersonasIdEndpoint import SystemInfoPersonasIdEndpoint
from pywise.endpoints.SystemInfoPersonasCountEndpoint import SystemInfoPersonasCountEndpoint
from pywise.models.PersonasInfoModel import PersonasInfoModel

class SystemInfoPersonasEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "personas", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemInfoPersonasCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemInfoPersonasIdEndpoint:
        child = SystemInfoPersonasIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PersonasInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PersonasInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PersonasInfoModel]:
        return self._parse_many(PersonasInfoModel, super().make_request("GET", params=params))
        