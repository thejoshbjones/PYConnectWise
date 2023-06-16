from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemParsingTypesIdEndpoint import SystemParsingTypesIdEndpoint
from pywise.endpoints.SystemParsingTypesCountEndpoint import SystemParsingTypesCountEndpoint
from pywise.models.ParsingTypeModel import ParsingTypeModel

class SystemParsingTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parsingTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemParsingTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemParsingTypesIdEndpoint:
        child = SystemParsingTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ParsingTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ParsingTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ParsingTypeModel]:
        return self._parse_many(ParsingTypeModel, super().make_request("GET", params=params))
        