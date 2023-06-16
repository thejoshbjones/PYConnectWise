from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyContactTypeAssociationsIdEndpoint import CompanyContactTypeAssociationsIdEndpoint
from pywise.endpoints.CompanyContactTypeAssociationsCountEndpoint import CompanyContactTypeAssociationsCountEndpoint
from pywise.models.ContactTypeAssociationModel import ContactTypeAssociationModel

class CompanyContactTypeAssociationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contactTypeAssociations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactTypeAssociationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyContactTypeAssociationsIdEndpoint:
        child = CompanyContactTypeAssociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ContactTypeAssociationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ContactTypeAssociationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ContactTypeAssociationModel]:
        return self._parse_many(ContactTypeAssociationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ContactTypeAssociationModel:
        return self._parse_one(ContactTypeAssociationModel, super().make_request("POST", params=params))
        