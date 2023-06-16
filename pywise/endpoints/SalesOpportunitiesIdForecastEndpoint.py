from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SalesOpportunitiesIdForecastIdEndpoint import SalesOpportunitiesIdForecastIdEndpoint
from pywise.endpoints.SalesOpportunitiesIdForecastCountEndpoint import SalesOpportunitiesIdForecastCountEndpoint
from pywise.models.ForecastModel import ForecastModel

class SalesOpportunitiesIdForecastEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SalesOpportunitiesIdForecastCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SalesOpportunitiesIdForecastIdEndpoint:
        child = SalesOpportunitiesIdForecastIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ForecastModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ForecastModel,
            self,
            page_size,
        )
    
    def delete(self, data=None, params=None) -> GenericMessageModel:
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params))
        
    def put(self, data=None, params=None) -> ForecastModel:
        return self._parse_one(ForecastModel, super().make_request("PUT", params=params))
        
    def patch(self, data=None, params=None) -> ForecastModel:
        return self._parse_one(ForecastModel, super().make_request("PATCH", params=params))
        