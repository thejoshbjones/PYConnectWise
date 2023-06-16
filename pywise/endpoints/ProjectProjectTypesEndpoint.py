from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectProjectTypesIdEndpoint import ProjectProjectTypesIdEndpoint
from pywise.endpoints.ProjectProjectTypesCountEndpoint import ProjectProjectTypesCountEndpoint
from pywise.endpoints.ProjectProjectTypesInfoEndpoint import ProjectProjectTypesInfoEndpoint
from pywise.models.ProjectTypeModel import ProjectTypeModel

class ProjectProjectTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "projectTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectProjectTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            ProjectProjectTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectProjectTypesIdEndpoint:
        child = ProjectProjectTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectTypeModel]:
        return self._parse_many(ProjectTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProjectTypeModel:
        return self._parse_one(ProjectTypeModel, super().make_request("POST", params=params))
        