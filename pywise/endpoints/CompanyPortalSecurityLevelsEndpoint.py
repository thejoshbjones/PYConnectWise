from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyPortalSecurityLevelsIdEndpoint import CompanyPortalSecurityLevelsIdEndpoint
from pywise.endpoints.CompanyPortalSecurityLevelsCountEndpoint import CompanyPortalSecurityLevelsCountEndpoint
from pywise.models.PortalSecurityLevelModel import PortalSecurityLevelModel

class CompanyPortalSecurityLevelsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "portalSecurityLevels", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyPortalSecurityLevelsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyPortalSecurityLevelsIdEndpoint:
        child = CompanyPortalSecurityLevelsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[PortalSecurityLevelModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            PortalSecurityLevelModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[PortalSecurityLevelModel]:
        return self._parse_many(PortalSecurityLevelModel, super().make_request("GET", params=params))
        