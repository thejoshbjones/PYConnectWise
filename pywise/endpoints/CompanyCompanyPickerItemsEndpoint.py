from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCompanyPickerItemsIdEndpoint import CompanyCompanyPickerItemsIdEndpoint
from pywise.endpoints.CompanyCompanyPickerItemsClearEndpoint import CompanyCompanyPickerItemsClearEndpoint
from pywise.endpoints.CompanyCompanyPickerItemsCountEndpoint import CompanyCompanyPickerItemsCountEndpoint
from pywise.models.CompanyPickerItemModel import CompanyPickerItemModel

class CompanyCompanyPickerItemsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "companyPickerItems", parent_endpoint=parent_endpoint)
        
        self.clear = self.register_child_endpoint(
            CompanyCompanyPickerItemsClearEndpoint(client, parent_endpoint=self)
        )
        self.count = self.register_child_endpoint(
            CompanyCompanyPickerItemsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCompanyPickerItemsIdEndpoint:
        child = CompanyCompanyPickerItemsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CompanyPickerItemModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CompanyPickerItemModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CompanyPickerItemModel]:
        return self._parse_many(CompanyPickerItemModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CompanyPickerItemModel:
        return self._parse_one(CompanyPickerItemModel, super().make_request("POST", params=params))
        