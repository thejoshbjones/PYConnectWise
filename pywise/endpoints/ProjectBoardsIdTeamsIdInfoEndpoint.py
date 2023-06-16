from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectBoardsIdTeamsIdInfoCountEndpoint import ProjectBoardsIdTeamsIdInfoCountEndpoint
from pywise.models.ProjectBoardTeamInfoModel import ProjectBoardTeamInfoModel

class ProjectBoardsIdTeamsIdInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.count = self.register_child_endpoint(
            ProjectBoardsIdTeamsIdInfoCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectBoardTeamInfoModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectBoardTeamInfoModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> ProjectBoardTeamInfoModel:
        return self._parse_one(ProjectBoardTeamInfoModel, super().make_request("GET", params=params))
        