from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemQuoteLinkSetupIdEndpoint import SystemQuoteLinkSetupIdEndpoint
from pywise.endpoints.SystemQuoteLinkSetupCountEndpoint import SystemQuoteLinkSetupCountEndpoint
from pywise.endpoints.SystemQuoteLinkSetupTestConnectionEndpoint import SystemQuoteLinkSetupTestConnectionEndpoint
from pywise.models.QuoteLinkModel import QuoteLinkModel

class SystemQuoteLinkSetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "quoteLinkSetup", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemQuoteLinkSetupCountEndpoint(client, parent_endpoint=self)
        )
        self.testConnection = self.register_child_endpoint(
            SystemQuoteLinkSetupTestConnectionEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemQuoteLinkSetupIdEndpoint:
        child = SystemQuoteLinkSetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[QuoteLinkModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            QuoteLinkModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[QuoteLinkModel]:
        return self._parse_many(QuoteLinkModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> QuoteLinkModel:
        return self._parse_one(QuoteLinkModel, super().make_request("POST", params=params))
        