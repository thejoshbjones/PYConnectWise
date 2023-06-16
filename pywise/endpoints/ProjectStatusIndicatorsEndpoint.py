from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectStatusIndicatorsIdEndpoint import ProjectStatusIndicatorsIdEndpoint
from pywise.endpoints.ProjectStatusIndicatorsCountEndpoint import ProjectStatusIndicatorsCountEndpoint
from pywise.models.StatusIndicatorModel import StatusIndicatorModel

class ProjectStatusIndicatorsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "statusIndicators", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectStatusIndicatorsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectStatusIndicatorsIdEndpoint:
        child = ProjectStatusIndicatorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[StatusIndicatorModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            StatusIndicatorModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[StatusIndicatorModel]:
        return self._parse_many(StatusIndicatorModel, super().make_request("GET", params=params))
        