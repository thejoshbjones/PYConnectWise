from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemOsgradeweightsIdEndpoint import SystemOsgradeweightsIdEndpoint
from pywise.endpoints.SystemOsgradeweightsCountEndpoint import SystemOsgradeweightsCountEndpoint
from pywise.models.OsGradeWeightModel import OsGradeWeightModel

class SystemOsgradeweightsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "osgradeweights", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemOsgradeweightsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemOsgradeweightsIdEndpoint:
        child = SystemOsgradeweightsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[OsGradeWeightModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            OsGradeWeightModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[OsGradeWeightModel]:
        return self._parse_many(OsGradeWeightModel, super().make_request("GET", params=params))
        