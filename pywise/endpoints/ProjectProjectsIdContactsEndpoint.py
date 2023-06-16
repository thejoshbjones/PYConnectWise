from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectProjectsIdContactsIdEndpoint import ProjectProjectsIdContactsIdEndpoint
from pywise.models.ProjectContactModel import ProjectContactModel

class ProjectProjectsIdContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contacts", parent_endpoint=parent_endpoint)
        
    
    def id(self, id: int) -> ProjectProjectsIdContactsIdEndpoint:
        child = ProjectProjectsIdContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectContactModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectContactModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectContactModel]:
        return self._parse_many(ProjectContactModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProjectContactModel:
        return self._parse_one(ProjectContactModel, super().make_request("POST", params=params))
        