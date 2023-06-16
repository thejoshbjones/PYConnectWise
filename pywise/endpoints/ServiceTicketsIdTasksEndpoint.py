from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.ServiceTicketsIdTasksIdEndpoint import ServiceTicketsIdTasksIdEndpoint
from pywise.endpoints.ServiceTicketsIdTasksCountEndpoint import ServiceTicketsIdTasksCountEndpoint
from pywise.models.TaskModel import TaskModel

class ServiceTicketsIdTasksEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tasks", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ServiceTicketsIdTasksCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> ServiceTicketsIdTasksIdEndpoint:
        child = ServiceTicketsIdTasksIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[TaskModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            TaskModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[TaskModel]:
        return self._parse_many(TaskModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> TaskModel:
        return self._parse_one(TaskModel, super().make_request("POST", params=params))
        