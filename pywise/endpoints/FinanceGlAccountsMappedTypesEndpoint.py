from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.FinanceGlAccountsMappedTypesCountEndpoint import FinanceGlAccountsMappedTypesCountEndpoint
from pywise.models.MappedTypeModel import MappedTypeModel

class FinanceGlAccountsMappedTypesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "mappedTypes", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceGlAccountsMappedTypesCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[MappedTypeModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            MappedTypeModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[MappedTypeModel]:
        return self._parse_many(MappedTypeModel, super().make_request("GET", params=params))
        