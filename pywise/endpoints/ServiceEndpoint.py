from pywise.endpoints.base.connectwise_top_level_endpoint import ConnectWiseEndpoint
from pywise.endpoints.ServiceBoardsEndpoint import ServiceBoardsEndpoint
from pywise.endpoints.ServiceCodesEndpoint import ServiceCodesEndpoint
from pywise.endpoints.ServiceEmailTemplatesEndpoint import ServiceEmailTemplatesEndpoint
from pywise.endpoints.ServiceImpactsEndpoint import ServiceImpactsEndpoint
from pywise.endpoints.ServiceKnowledgeBaseArticlesEndpoint import ServiceKnowledgeBaseArticlesEndpoint
from pywise.endpoints.ServiceKnowledgeBaseCategoriesEndpoint import ServiceKnowledgeBaseCategoriesEndpoint
from pywise.endpoints.ServiceKnowledgebasesettingsEndpoint import ServiceKnowledgebasesettingsEndpoint
from pywise.endpoints.ServiceKnowledgeBaseSubCategoriesEndpoint import ServiceKnowledgeBaseSubCategoriesEndpoint
from pywise.endpoints.ServiceLocationsEndpoint import ServiceLocationsEndpoint
from pywise.endpoints.ServicePrioritiesEndpoint import ServicePrioritiesEndpoint
from pywise.endpoints.ServiceServiceSignoffEndpoint import ServiceServiceSignoffEndpoint
from pywise.endpoints.ServiceSeveritiesEndpoint import ServiceSeveritiesEndpoint
from pywise.endpoints.ServiceSLAsEndpoint import ServiceSLAsEndpoint
from pywise.endpoints.ServiceSourcesEndpoint import ServiceSourcesEndpoint
from pywise.endpoints.ServiceSurveysEndpoint import ServiceSurveysEndpoint
from pywise.endpoints.ServiceTeamMembersEndpoint import ServiceTeamMembersEndpoint
from pywise.endpoints.ServiceTeamsEndpoint import ServiceTeamsEndpoint
from pywise.endpoints.ServiceTemplatesEndpoint import ServiceTemplatesEndpoint
from pywise.endpoints.ServiceTicketLinksEndpoint import ServiceTicketLinksEndpoint
from pywise.endpoints.ServiceTicketsEndpoint import ServiceTicketsEndpoint
from pywise.endpoints.ServiceTicketSyncsEndpoint import ServiceTicketSyncsEndpoint

class ServiceEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "service")
        
        self.boards = self.register_child_endpoint(
            ServiceBoardsEndpoint(client, parent_endpoint=self)
        )
        self.codes = self.register_child_endpoint(
            ServiceCodesEndpoint(client, parent_endpoint=self)
        )
        self.emailTemplates = self.register_child_endpoint(
            ServiceEmailTemplatesEndpoint(client, parent_endpoint=self)
        )
        self.impacts = self.register_child_endpoint(
            ServiceImpactsEndpoint(client, parent_endpoint=self)
        )
        self.knowledgeBaseArticles = self.register_child_endpoint(
            ServiceKnowledgeBaseArticlesEndpoint(client, parent_endpoint=self)
        )
        self.knowledgeBaseCategories = self.register_child_endpoint(
            ServiceKnowledgeBaseCategoriesEndpoint(client, parent_endpoint=self)
        )
        self.knowledgebasesettings = self.register_child_endpoint(
            ServiceKnowledgebasesettingsEndpoint(client, parent_endpoint=self)
        )
        self.knowledgeBaseSubCategories = self.register_child_endpoint(
            ServiceKnowledgeBaseSubCategoriesEndpoint(client, parent_endpoint=self)
        )
        self.locations = self.register_child_endpoint(
            ServiceLocationsEndpoint(client, parent_endpoint=self)
        )
        self.priorities = self.register_child_endpoint(
            ServicePrioritiesEndpoint(client, parent_endpoint=self)
        )
        self.serviceSignoff = self.register_child_endpoint(
            ServiceServiceSignoffEndpoint(client, parent_endpoint=self)
        )
        self.severities = self.register_child_endpoint(
            ServiceSeveritiesEndpoint(client, parent_endpoint=self)
        )
        self.SLAs = self.register_child_endpoint(
            ServiceSLAsEndpoint(client, parent_endpoint=self)
        )
        self.sources = self.register_child_endpoint(
            ServiceSourcesEndpoint(client, parent_endpoint=self)
        )
        self.surveys = self.register_child_endpoint(
            ServiceSurveysEndpoint(client, parent_endpoint=self)
        )
        self.teamMembers = self.register_child_endpoint(
            ServiceTeamMembersEndpoint(client, parent_endpoint=self)
        )
        self.teams = self.register_child_endpoint(
            ServiceTeamsEndpoint(client, parent_endpoint=self)
        )
        self.templates = self.register_child_endpoint(
            ServiceTemplatesEndpoint(client, parent_endpoint=self)
        )
        self.ticketLinks = self.register_child_endpoint(
            ServiceTicketLinksEndpoint(client, parent_endpoint=self)
        )
        self.tickets = self.register_child_endpoint(
            ServiceTicketsEndpoint(client, parent_endpoint=self)
        )
        self.ticketSyncs = self.register_child_endpoint(
            ServiceTicketSyncsEndpoint(client, parent_endpoint=self)
        )