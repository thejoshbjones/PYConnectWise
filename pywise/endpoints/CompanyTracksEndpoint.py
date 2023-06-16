from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyTracksIdEndpoint import CompanyTracksIdEndpoint
from pywise.endpoints.CompanyTracksCountEndpoint import CompanyTracksCountEndpoint
from pywise.models.TrackModel import TrackModel

class CompanyTracksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tracks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyTracksCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyTracksIdEndpoint:
        child = CompanyTracksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TrackModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TrackModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TrackModel]:
        return self._parse_many(TrackModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TrackModel:
        return self._parse_one(TrackModel, super().make_request("POST", params=params))
        