from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceBoardsIdAutoTemplatesIdEndpoint import ServiceBoardsIdAutoTemplatesIdEndpoint
from pywise.endpoints.ServiceBoardsIdAutoTemplatesCountEndpoint import ServiceBoardsIdAutoTemplatesCountEndpoint
from pywise.models.BoardAutoTemplateModel import BoardAutoTemplateModel

class ServiceBoardsIdAutoTemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "autoTemplates", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceBoardsIdAutoTemplatesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceBoardsIdAutoTemplatesIdEndpoint:
        child = ServiceBoardsIdAutoTemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BoardAutoTemplateModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BoardAutoTemplateModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[BoardAutoTemplateModel]:
        return self._parse_many(BoardAutoTemplateModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> BoardAutoTemplateModel:
        return self._parse_one(BoardAutoTemplateModel, super().make_request("POST", params=params))
        