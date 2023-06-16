from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyAddressFormatsIdEndpoint import CompanyAddressFormatsIdEndpoint
from pywise.endpoints.CompanyAddressFormatsCountEndpoint import CompanyAddressFormatsCountEndpoint
from pywise.endpoints.CompanyAddressFormatsInfoEndpoint import CompanyAddressFormatsInfoEndpoint
from pywise.models.AddressFormatModel import AddressFormatModel

class CompanyAddressFormatsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "addressFormats", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyAddressFormatsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyAddressFormatsInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyAddressFormatsIdEndpoint:
        child = CompanyAddressFormatsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[AddressFormatModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            AddressFormatModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[AddressFormatModel]:
        return self._parse_many(AddressFormatModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> AddressFormatModel:
        return self._parse_one(AddressFormatModel, super().make_request("POST", params=params))
        