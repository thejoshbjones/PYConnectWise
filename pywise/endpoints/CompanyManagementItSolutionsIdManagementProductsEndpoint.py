from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyManagementItSolutionsIdManagementProductsIdEndpoint import CompanyManagementItSolutionsIdManagementProductsIdEndpoint
from pywise.endpoints.CompanyManagementItSolutionsIdManagementProductsCountEndpoint import CompanyManagementItSolutionsIdManagementProductsCountEndpoint
from pywise.models.ManagementItSolutionAgreementInterfaceParameterModel import ManagementItSolutionAgreementInterfaceParameterModel

class CompanyManagementItSolutionsIdManagementProductsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "managementProducts", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyManagementItSolutionsIdManagementProductsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyManagementItSolutionsIdManagementProductsIdEndpoint:
        child = CompanyManagementItSolutionsIdManagementProductsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ManagementItSolutionAgreementInterfaceParameterModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ManagementItSolutionAgreementInterfaceParameterModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ManagementItSolutionAgreementInterfaceParameterModel]:
        return self._parse_many(ManagementItSolutionAgreementInterfaceParameterModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> ManagementItSolutionAgreementInterfaceParameterModel:
        return self._parse_one(ManagementItSolutionAgreementInterfaceParameterModel, super().make_request("POST", params=params))
        