from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCommunicationTypesIdEndpoint import CompanyCommunicationTypesIdEndpoint
from pywise.endpoints.CompanyCommunicationTypesCountEndpoint import CompanyCommunicationTypesCountEndpoint
from pywise.endpoints.CompanyCommunicationTypesInfoEndpoint import CompanyCommunicationTypesInfoEndpoint
from pywise.models.CommunicationTypeModel import CommunicationTypeModel

class CompanyCommunicationTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "communicationTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCommunicationTypesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyCommunicationTypesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCommunicationTypesIdEndpoint:
        child = CompanyCommunicationTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CommunicationTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CommunicationTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CommunicationTypeModel]:
        return self._parse_many(CommunicationTypeModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CommunicationTypeModel:
        return self._parse_one(CommunicationTypeModel, super().make_request("POST", params=params))
        