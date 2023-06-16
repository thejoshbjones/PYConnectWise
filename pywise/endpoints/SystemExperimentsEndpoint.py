from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemExperimentsIdEndpoint import SystemExperimentsIdEndpoint
from pywise.endpoints.SystemExperimentsCountEndpoint import SystemExperimentsCountEndpoint
from pywise.models.ExperimentModel import ExperimentModel

class SystemExperimentsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "experiments", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemExperimentsCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemExperimentsIdEndpoint:
        child = SystemExperimentsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[ExperimentModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            ExperimentModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[ExperimentModel]:
        return self._parse_many(ExperimentModel, super().make_request("GET", params=params))
        