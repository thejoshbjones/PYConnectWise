from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.CompanyConfigurationsStatusesIdUsagesListEndpoint import CompanyConfigurationsStatusesIdUsagesListEndpoint
from pywise.models.UsageModel import UsageModel

class CompanyConfigurationsStatusesIdUsagesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "usages", parent_endpoint=parent_endpoint, id_index="{id}")
        
        self.list = self.register_child_endpoint(
            CompanyConfigurationsStatusesIdUsagesListEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[UsageModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            UsageModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[UsageModel]:
        return self._parse_many(UsageModel, super().make_request("GET", params=params))
        