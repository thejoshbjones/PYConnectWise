from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMyAccountIdDelegationsIdEndpoint import SystemMyAccountIdDelegationsIdEndpoint
from pywise.endpoints.SystemMyAccountIdDelegationsCountEndpoint import SystemMyAccountIdDelegationsCountEndpoint
from pywise.models.MemberDelegationModel import MemberDelegationModel

class SystemMyAccountIdDelegationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "delegations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyAccountIdDelegationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMyAccountIdDelegationsIdEndpoint:
        child = SystemMyAccountIdDelegationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberDelegationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberDelegationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MemberDelegationModel]:
        return self._parse_many(MemberDelegationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MemberDelegationModel:
        return self._parse_one(MemberDelegationModel, super().make_request("POST", params=params))
        