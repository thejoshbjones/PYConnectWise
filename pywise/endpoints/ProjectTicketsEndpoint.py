from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ProjectTicketsIdEndpoint import ProjectTicketsIdEndpoint
from pywise.endpoints.ProjectTicketsCountEndpoint import ProjectTicketsCountEndpoint
from pywise.endpoints.ProjectTicketsSearchEndpoint import ProjectTicketsSearchEndpoint
from pywise.models.ProjectTicketModel import ProjectTicketModel

class ProjectTicketsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tickets", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProjectTicketsCountEndpoint(client, parent_endpoint=self)
        )
        self.search = self.register_child_endpoint(
            ProjectTicketsSearchEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ProjectTicketsIdEndpoint:
        child = ProjectTicketsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ProjectTicketModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ProjectTicketModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ProjectTicketModel]:
        return self._parse_many(ProjectTicketModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ProjectTicketModel:
        return self._parse_one(ProjectTicketModel, super().make_request("POST", params=params))
        