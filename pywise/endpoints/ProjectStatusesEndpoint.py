from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectStatusesIdEndpoint import ProjectStatusesIdEndpoint
from pywise.endpoints.ProjectStatusesCountEndpoint import ProjectStatusesCountEndpoint
from pywise.endpoints.ProjectStatusesInfoEndpoint import ProjectStatusesInfoEndpoint
from pywise.models.ProjectStatusModel import ProjectStatusModel

class ProjectStatusesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statuses", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectStatusesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProjectStatusesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectStatusesIdEndpoint:
        child = ProjectStatusesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectStatusModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectStatusModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectStatusModel]:
        return self._parse_many(ProjectStatusModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProjectStatusModel:
        return self._parse_one(ProjectStatusModel, super().make_request("POST", params=params))
        