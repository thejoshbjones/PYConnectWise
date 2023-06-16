from pywise.models.base.message_model import GenericMessageModel
from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.responses.paginated_response import PaginatedResponse
from pywise.endpoints.SystemSkillCategoriesIdEndpoint import SystemSkillCategoriesIdEndpoint
from pywise.endpoints.SystemSkillCategoriesCountEndpoint import SystemSkillCategoriesCountEndpoint
from pywise.models.SkillCategoryModel import SkillCategoryModel

class SystemSkillCategoriesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "skillCategories", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemSkillCategoriesCountEndpoint(client, parent_endpoint=self)
        )
    
    def id(self, id: int) -> SystemSkillCategoriesIdEndpoint:
        child = SystemSkillCategoriesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params={}) -> PaginatedResponse[SkillCategoryModel]:
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params,
                as_json=False,
            ),
            SkillCategoryModel,
            self,
            page_size,
        )
    
    def get(self, data=None, params=None) -> list[SkillCategoryModel]:
        return self._parse_many(SkillCategoryModel, super().make_request("GET", params=params))
        
    def post(self, data=None, params=None) -> SkillCategoryModel:
        return self._parse_one(SkillCategoryModel, super().make_request("POST", params=params))
        