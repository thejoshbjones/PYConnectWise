from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.MemberDeactivationModel import MemberDeactivationModel

class SystemMembersIdDeactivateEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "deactivate", parent_endpoint=parent_endpoint, id_index="{id}")
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberDeactivationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberDeactivationModel,
            self,
            page_size,
        )
    
    def post(self, data=None, params=None) -> MemberDeactivationModel:
        return self._parse_one(MemberDeactivationModel, super().make_request("POST", params=params))
        