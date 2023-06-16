from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyContactsDepartmentsIdEndpoint import CompanyContactsDepartmentsIdEndpoint
from pywise.endpoints.CompanyContactsDepartmentsCountEndpoint import CompanyContactsDepartmentsCountEndpoint
from pywise.endpoints.CompanyContactsDepartmentsInfoEndpoint import CompanyContactsDepartmentsInfoEndpoint
from pywise.models.ContactDepartmentModel import ContactDepartmentModel

class CompanyContactsDepartmentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "departments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyContactsDepartmentsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyContactsDepartmentsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyContactsDepartmentsIdEndpoint:
        child = CompanyContactsDepartmentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ContactDepartmentModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ContactDepartmentModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ContactDepartmentModel]:
        return self._parse_many(ContactDepartmentModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ContactDepartmentModel:
        return self._parse_one(ContactDepartmentModel, super().make_request("POST", params=params))
        