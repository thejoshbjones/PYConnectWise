from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompaniesIdTracksIdEndpoint import CompanyCompaniesIdTracksIdEndpoint
from pywise.endpoints.CompanyCompaniesIdTracksCountEndpoint import CompanyCompaniesIdTracksCountEndpoint
from pywise.models.ContactTrackModel import ContactTrackModel

class CompanyCompaniesIdTracksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tracks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompaniesIdTracksCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompaniesIdTracksIdEndpoint:
        child = CompanyCompaniesIdTracksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ContactTrackModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ContactTrackModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ContactTrackModel]:
        return self._parse_many(ContactTrackModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ContactTrackModel:
        return self._parse_one(ContactTrackModel, super().make_request("POST", params=params))
        