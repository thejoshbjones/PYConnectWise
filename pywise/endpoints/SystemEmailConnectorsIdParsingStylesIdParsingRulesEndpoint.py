from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemEmailConnectorsIdParsingStylesIdParsingRulesIdEndpoint import SystemEmailConnectorsIdParsingStylesIdParsingRulesIdEndpoint
from pywise.endpoints.SystemEmailConnectorsIdParsingStylesIdParsingRulesCountEndpoint import SystemEmailConnectorsIdParsingStylesIdParsingRulesCountEndpoint
from pywise.models.EmailConnectorParsingRuleModel import EmailConnectorParsingRuleModel

class SystemEmailConnectorsIdParsingStylesIdParsingRulesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "parsingRules", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemEmailConnectorsIdParsingStylesIdParsingRulesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemEmailConnectorsIdParsingStylesIdParsingRulesIdEndpoint:
        child = SystemEmailConnectorsIdParsingStylesIdParsingRulesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[EmailConnectorParsingRuleModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            EmailConnectorParsingRuleModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[EmailConnectorParsingRuleModel]:
        return self._parse_many(EmailConnectorParsingRuleModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> EmailConnectorParsingRuleModel:
        return self._parse_one(EmailConnectorParsingRuleModel, super().make_request("POST", params=params))
        