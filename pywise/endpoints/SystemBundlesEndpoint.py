from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemBundlesCountEndpoint import SystemBundlesCountEndpoint
from pywise.models.BundleResultsCollectionModel import BundleResultsCollectionModel

class SystemBundlesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "bundles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemBundlesCountEndpoint(client, parent_endpoint=self)
        )
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[BundleResultsCollectionModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            BundleResultsCollectionModel,
            self,
            page_size,
        )
    
    def post(self, data=None, params=None) -> BundleResultsCollectionModel:
        return self._parse_one(BundleResultsCollectionModel, super().make_request("POST", params=params))
        