from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemMembersIdMycertificationsIdEndpoint import SystemMembersIdMycertificationsIdEndpoint
from pywise.endpoints.SystemMembersIdMycertificationsCountEndpoint import SystemMembersIdMycertificationsCountEndpoint
from pywise.models.MemberCertificationModel import MemberCertificationModel

class SystemMembersIdMycertificationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "mycertifications", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMembersIdMycertificationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemMembersIdMycertificationsIdEndpoint:
        child = SystemMembersIdMycertificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MemberCertificationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MemberCertificationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MemberCertificationModel]:
        return self._parse_many(MemberCertificationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> MemberCertificationModel:
        return self._parse_one(MemberCertificationModel, super().make_request("POST", params=params))
        