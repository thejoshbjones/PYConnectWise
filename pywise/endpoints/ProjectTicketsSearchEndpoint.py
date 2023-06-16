from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.ProjectTicketModel import ProjectTicketModel

class ProjectTicketsSearchEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "search", parent_endpoint=parent_endpoint)
        
    
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
    
    def post(self, data=None, params=None) -> list[ProjectTicketModel]:
        return self._parse_many(ProjectTicketModel, super().make_request("POST", params=params))
        