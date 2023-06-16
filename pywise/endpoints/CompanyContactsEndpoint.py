from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyContactsIdEndpoint import CompanyContactsIdEndpoint
from pywise.endpoints.CompanyContactsCountEndpoint import CompanyContactsCountEndpoint
from pywise.endpoints.CompanyContactsDefaultEndpoint import CompanyContactsDefaultEndpoint
from pywise.endpoints.CompanyContactsDepartmentsEndpoint import CompanyContactsDepartmentsEndpoint
from pywise.endpoints.CompanyContactsRelationshipsEndpoint import CompanyContactsRelationshipsEndpoint
from pywise.endpoints.CompanyContactsRequestPasswordEndpoint import CompanyContactsRequestPasswordEndpoint
from pywise.endpoints.CompanyContactsTypesEndpoint import CompanyContactsTypesEndpoint
from pywise.endpoints.CompanyContactsValidatePortalCredentialsEndpoint import CompanyContactsValidatePortalCredentialsEndpoint
from pywise.models.ContactModel import ContactModel

class CompanyContactsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "contacts", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsCountEndpoint(client, parent_endpoint=self)
        )
        self.default = self.register_child_endpoint(
            CompanyContactsDefaultEndpoint(client, parent_endpoint=self)
        )
        self.departments = self.register_child_endpoint(
            CompanyContactsDepartmentsEndpoint(client, parent_endpoint=self)
        )
        self.relationships = self.register_child_endpoint(
            CompanyContactsRelationshipsEndpoint(client, parent_endpoint=self)
        )
        self.requestPassword = self.register_child_endpoint(
            CompanyContactsRequestPasswordEndpoint(client, parent_endpoint=self)
        )
        self.types = self.register_child_endpoint(
            CompanyContactsTypesEndpoint(client, parent_endpoint=self)
        )
        self.validatePortalCredentials = self.register_child_endpoint(
            CompanyContactsValidatePortalCredentialsEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyContactsIdEndpoint:
        child = CompanyContactsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ContactModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ContactModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ContactModel]:
        return self._parse_many(ContactModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ContactModel:
        return self._parse_one(ContactModel, super().make_request("POST", params=params))
        