from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompanyTypeAssociationsIdEndpoint import CompanyCompanyTypeAssociationsIdEndpoint
from pywise.endpoints.CompanyCompanyTypeAssociationsCountEndpoint import CompanyCompanyTypeAssociationsCountEndpoint
from pywise.models.CompanyTypeAssociationModel import CompanyTypeAssociationModel

class CompanyCompanyTypeAssociationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companyTypeAssociations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCompanyTypeAssociationsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompanyTypeAssociationsIdEndpoint:
        child = CompanyCompanyTypeAssociationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyTypeAssociationModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyTypeAssociationModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyTypeAssociationModel]:
        return self._parse_many(CompanyTypeAssociationModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanyTypeAssociationModel:
        return self._parse_one(CompanyTypeAssociationModel, super().make_request("POST", params=params))
        