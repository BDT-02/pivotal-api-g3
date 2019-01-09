from src.pivotal_api_services.pivotal_services import PivotalServices
from src.utils.LoggerHandler import LoggerHandler
from src.utils.file_reader import FileReader
from src.utils.string_handler import StringHandler

logger = LoggerHandler.get_instance()
class WorkspacesServices(PivotalServices):

    def __init__(self):
        super(WorkspacesServices, self).__init__()
        self.__workspace = "{}/accounts".format(self.request_handler.main_url)
        self.__workspace_schema_path = "/src/core/api/json_schemas/project_schema.json"
        self.workspace = {}
        self.workspace = {}

    def create_workspace(self, data):
        response = self.request_handler.post_request(endpoint=self.__workspace, body=data)
        return response.status_code, response.json()

    def get_workspace(self):
        workspace_list = self.request_handler.get_request(endpoint=self.__workspace).json()
        for workspace in workspace_list:
            if not workspace['name'] in self.workspace:
                self.workspaces[workspace['name']] = workspace['id']
        return self.workspaces

    def get_workspace(self, id):
        current_url = self.__workspace + "/" + id
        workspace = self.request_handler.get_request(endpoint=current_url).json()
        if not workspace['name'] in self.workspaces:
            self.workspaces[workspace['name']] = workspace['id']
        return workspace

    def get_workspace_schema(self):
        return StringHandler.convert_string_to_json(FileReader.get_file_content(self.__workspace_schema_path))

  #  def delete_all_projects(self):
   #     self.get_projects()
    #    for project in self.projects.values():
     #       url = self.__project + "/" + str(project)
      #      logger.info("Deleting %s" % url)
       #     self.request_handler.delete_request(endpoint=url)
