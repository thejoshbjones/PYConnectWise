from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemGoogleemailsetupIdEndpoint import SystemGoogleemailsetupIdEndpoint
from pywise.endpoints.SystemGoogleemailsetupCountEndpoint import SystemGoogleemailsetupCountEndpoint
from pywise.models.GoogleEmailSetupModel import GoogleEmailSetupModel

class SystemGoogleemailsetupEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemGoogleemailsetupCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemGoogleemailsetupIdEndpoint:
        child = SystemGoogleemailsetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[GoogleEmailSetupModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            GoogleEmailSetupModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[GoogleEmailSetupModel]:
        return self._parse_many(GoogleEmailSetupModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> GoogleEmailSetupModel:
        return self._parse_one(GoogleEmailSetupModel, super().make_request("POST", params=params))
        