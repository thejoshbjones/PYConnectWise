from pywise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pywise.endpoints.manage.ServiceBoardsEndpoint import ServiceBoardsEndpoint
from pywise.endpoints.manage.ServiceCodesEndpoint import ServiceCodesEndpoint
from pywise.endpoints.manage.ServiceEmailTemplatesEndpoint import ServiceEmailTemplatesEndpoint
from pywise.endpoints.manage.ServiceImpactsEndpoint import ServiceImpactsEndpoint
from pywise.endpoints.manage.ServiceKnowledgeBaseArticlesEndpoint import ServiceKnowledgeBaseArticlesEndpoint
from pywise.endpoints.manage.ServiceKnowledgeBaseCategoriesEndpoint import ServiceKnowledgeBaseCategoriesEndpoint
from pywise.endpoints.manage.ServiceKnowledgebasesettingsEndpoint import ServiceKnowledgebasesettingsEndpoint
from pywise.endpoints.manage.ServiceKnowledgeBaseSubCategoriesEndpoint import ServiceKnowledgeBaseSubCategoriesEndpoint
from pywise.endpoints.manage.ServiceLocationsEndpoint import ServiceLocationsEndpoint
from pywise.endpoints.manage.ServicePrioritiesEndpoint import ServicePrioritiesEndpoint
from pywise.endpoints.manage.ServiceServiceSignoffEndpoint import ServiceServiceSignoffEndpoint
from pywise.endpoints.manage.ServiceSeveritiesEndpoint import ServiceSeveritiesEndpoint
from pywise.endpoints.manage.ServiceSLAsEndpoint import ServiceSLAsEndpoint
from pywise.endpoints.manage.ServiceSourcesEndpoint import ServiceSourcesEndpoint
from pywise.endpoints.manage.ServiceSurveysEndpoint import ServiceSurveysEndpoint
from pywise.endpoints.manage.ServiceTeamMembersEndpoint import ServiceTeamMembersEndpoint
from pywise.endpoints.manage.ServiceTeamsEndpoint import ServiceTeamsEndpoint
from pywise.endpoints.manage.ServiceTemplatesEndpoint import ServiceTemplatesEndpoint
from pywise.endpoints.manage.ServiceTicketLinksEndpoint import ServiceTicketLinksEndpoint
from pywise.endpoints.manage.ServiceTicketsEndpoint import ServiceTicketsEndpoint
from pywise.endpoints.manage.ServiceTicketSyncsEndpoint import ServiceTicketSyncsEndpoint

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