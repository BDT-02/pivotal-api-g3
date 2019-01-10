from src.pivotal_api_services.projects import ProjectServices
from src.utils.LoggerHandler import LoggerHandler

logger = LoggerHandler.get_instance()


def after_scenario(context, scenario):
    if 'delete_project' in scenario.tags:
        project_services = ProjectServices()
        project_services.delete_all_projects()
        logger.info("Delete all project created")
    if 'Test':
        print '/////////////G3 SCENARIO TESTED///////////////////'
