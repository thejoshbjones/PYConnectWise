from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemManagementNetworkSecuritiesIdEndpoint import SystemManagementNetworkSecuritiesIdEndpoint
from pywise.endpoints.SystemManagementNetworkSecuritiesCountEndpoint import SystemManagementNetworkSecuritiesCountEndpoint
from pywise.models.ManagementNetworkSecurityModel import ManagementNetworkSecurityModel

class SystemManagementNetworkSecuritiesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementNetworkSecurities", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemManagementNetworkSecuritiesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemManagementNetworkSecuritiesIdEndpoint:
        child = SystemManagementNetworkSecuritiesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagementNetworkSecurityModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagementNetworkSecurityModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagementNetworkSecurityModel]:
        return self._parse_many(ManagementNetworkSecurityModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ManagementNetworkSecurityModel:
        return self._parse_one(ManagementNetworkSecurityModel, super().make_request("POST", params=params))
        