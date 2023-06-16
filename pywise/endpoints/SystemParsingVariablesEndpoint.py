from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemParsingVariablesIdEndpoint import SystemParsingVariablesIdEndpoint
from pywise.endpoints.SystemParsingVariablesCountEndpoint import SystemParsingVariablesCountEndpoint
from pywise.models.ParsingVariableModel import ParsingVariableModel

class SystemParsingVariablesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parsingVariables", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemParsingVariablesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemParsingVariablesIdEndpoint:
        child = SystemParsingVariablesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ParsingVariableModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ParsingVariableModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ParsingVariableModel]:
        return self._parse_many(ParsingVariableModel, super().make_request("GET", params=params))
        