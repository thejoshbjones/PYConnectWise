from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyTracksIdActionsIdEndpoint import CompanyTracksIdActionsIdEndpoint
from pywise.endpoints.CompanyTracksIdActionsCountEndpoint import CompanyTracksIdActionsCountEndpoint
from pywise.models.TrackActionModel import TrackActionModel

class CompanyTracksIdActionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "actions", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyTracksIdActionsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyTracksIdActionsIdEndpoint:
        child = CompanyTracksIdActionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TrackActionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TrackActionModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TrackActionModel]:
        return self._parse_many(TrackActionModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TrackActionModel:
        return self._parse_one(TrackActionModel, super().make_request("POST", params=params))
        