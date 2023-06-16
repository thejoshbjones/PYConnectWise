from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemEmailConnectorsIdParsingStylesIdEndpoint import SystemEmailConnectorsIdParsingStylesIdEndpoint
from pywise.endpoints.SystemEmailConnectorsIdParsingStylesCountEndpoint import SystemEmailConnectorsIdParsingStylesCountEndpoint
from pywise.models.EmailConnectorParsingStyleModel import EmailConnectorParsingStyleModel

class SystemEmailConnectorsIdParsingStylesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parsingStyles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemEmailConnectorsIdParsingStylesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemEmailConnectorsIdParsingStylesIdEndpoint:
        child = SystemEmailConnectorsIdParsingStylesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[EmailConnectorParsingStyleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            EmailConnectorParsingStyleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[EmailConnectorParsingStyleModel]:
        return self._parse_many(EmailConnectorParsingStyleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> EmailConnectorParsingStyleModel:
        return self._parse_one(EmailConnectorParsingStyleModel, super().make_request("POST", params=params))
        