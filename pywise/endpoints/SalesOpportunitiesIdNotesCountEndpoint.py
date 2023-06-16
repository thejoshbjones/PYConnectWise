from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.models.OpportunityNoteModel import OpportunityNoteModel

class SalesOpportunitiesIdNotesCountEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "count", parent_endpoint=parent_endpoint)
        
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OpportunityNoteModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OpportunityNoteModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OpportunityNoteModel]:
        return self._parse_many(OpportunityNoteModel, super().make_request("GET", params=params))
        