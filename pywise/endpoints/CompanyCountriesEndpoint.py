from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyCountriesIdEndpoint import CompanyCountriesIdEndpoint
from pywise.endpoints.CompanyCountriesCountEndpoint import CompanyCountriesCountEndpoint
from pywise.endpoints.CompanyCountriesInfoEndpoint import CompanyCountriesInfoEndpoint
from pywise.models.CountryModel import CountryModel

class CompanyCountriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "countries", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            CompanyCountriesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            CompanyCountriesInfoEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> CompanyCountriesIdEndpoint:
        child = CompanyCountriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[CountryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            CountryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[CountryModel]:
        return self._parse_many(CountryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> CountryModel:
        return self._parse_one(CountryModel, super().make_request("POST", params=params))
        