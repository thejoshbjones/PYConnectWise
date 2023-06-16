from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOpportunitiesIdNotesIdEndpoint import SalesOpportunitiesIdNotesIdEndpoint
from pywise.endpoints.SalesOpportunitiesIdNotesCountEndpoint import SalesOpportunitiesIdNotesCountEndpoint
from pywise.models.OpportunityNoteModel import OpportunityNoteModel

class SalesOpportunitiesIdNotesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "notes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesIdNotesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOpportunitiesIdNotesIdEndpoint:
        child = SalesOpportunitiesIdNotesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
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
        
    def post(self, data=None, params=None) -> OpportunityNoteModel:
        return self._parse_one(OpportunityNoteModel, super().make_request("POST", params=params))
        