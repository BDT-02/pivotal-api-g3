from src.pivotal_api_services.pivotal_services import PivotalServices
from src.utils.LoggerHandler import LoggerHandler
from src.utils.file_reader import FileReader
from src.utils.string_handler import StringHandler

logger = LoggerHandler.get_instance()
class WorkspacesServices(PivotalServices):

    def __init__(self):
        super(WorkspacesServices, self).__init__()
        self.__account = "{}/accounts".format(self.request_handler.main_url)
        self.__account_schema_path = "/src/core/api/json_schemas/project_schema.json"
        self.account = {}
        self.accounts = {}

    def create_account(self, data):
        response = self.request_handler.post_request(endpoint=self.__account, body=data)
        return response.status_code, response.json()

    def get_accounts(self):
        account_list = self.request_handler.get_request(endpoint=self.__account).json()
        for account in account_list:
            if not account['name'] in self.accounts:
                self.accounts[account['name']] = account['id']
        return self.accounts

    def get_account(self, id):
        current_url = self.__account + "/" + id
        account = self.request_handler.get_request(endpoint=current_url).json()
        if not account['name'] in self.accounts:
            self.accounts[account['name']] = account['id']
        return account

    def get_account_schema(self):
        return StringHandler.convert_string_to_json(FileReader.get_file_content(self.__account_schema_path))

  #  def delete_all_projects(self):
   #     self.get_projects()
    #    for project in self.projects.values():
     #       url = self.__project + "/" + str(project)
      #      logger.info("Deleting %s" % url)
       #     self.request_handler.delete_request(endpoint=url)
