from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMyAccountIdDelegationsEndpoint import SystemMyAccountIdDelegationsEndpoint
from pywise.endpoints.SystemMyAccountIdSkillsEndpoint import SystemMyAccountIdSkillsEndpoint
from pywise.models.MyAccountModel import MyAccountModel

class SystemMyAccountIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.delegations = self.register_child_endpoint(
            SystemMyAccountIdDelegationsEndpoint(client, parent_endpoint=self)
        )
        self.skills = self.register_child_endpoint(
            SystemMyAccountIdSkillsEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MyAccountModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MyAccountModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> MyAccountModel:
        return self._parse_one(MyAccountModel, super().make_request("GET", params=params))
        
    def put(self, data=None, params=None) -> MyAccountModel:
        return self._parse_one(MyAccountModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> MyAccountModel:
        return self._parse_one(MyAccountModel, super().make_request("PATCH", params=params))
        