from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectTicketsIdTasksIdEndpoint import ProjectTicketsIdTasksIdEndpoint
from pywise.endpoints.ProjectTicketsIdTasksCountEndpoint import ProjectTicketsIdTasksCountEndpoint
from pywise.models.TicketTaskModel import TicketTaskModel

class ProjectTicketsIdTasksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tasks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectTicketsIdTasksCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectTicketsIdTasksIdEndpoint:
        child = ProjectTicketsIdTasksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TicketTaskModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TicketTaskModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TicketTaskModel]:
        return self._parse_many(TicketTaskModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TicketTaskModel:
        return self._parse_one(TicketTaskModel, super().make_request("POST", params=params))
        