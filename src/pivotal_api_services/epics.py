from src.pivotal_api_services.pivotal_services import PivotalServices
from src.utils.LoggerHandler import LoggerHandler
# from src.utils.file_reader import FileReader
from src.utils.file_reader import FileReader
from src.utils.string_handler import StringHandler

logger = LoggerHandler.get_instance()


class EpicServices(PivotalServices):

    def __init__(self):
        super(EpicServices, self).__init__()
        self.endPoint = "{}/projects/{}".format(self.request_handler.main_url, "{}/epics")
        print self.endPoint
        self.__epic_schema_path = "/src/core/api/json_schemas/epics_schema.json"
        self.epic = {}
        self.epics = {}

    def create_epic(self, id_project, data):
        current_url = self.endPoint.format(id_project)
        print data
        response = self.request_handler.post_request(endpoint=current_url, body=data)
        return response.status_code, response.json()

    def update_epic(self, id_project, id_epic, data):
        current_url = self.endPoint.format(id_project) + "/" + id_epic
        response = self.request_handler.put_request(endpoint=current_url, body=data)
        return response.status_code, response.json()

    def get_epics(self):
        epic_list = self.request_handler.get_request(endpoint=self.__epic).json()
        for epic in epic_list:
            if not epic['name'] in self.epics:
                self.epics[epic['name']] = epic['id']
        return self.epics

    def get_epic(self, id_project, id_epic):
        current_url = self.endPoint.format(id_project) + "/" + id_epic
        epic = self.request_handler.get_request(endpoint=current_url).json()
        if not epic['name'] in self.epics:
            self.epics[epic['name']] = epic['id']
        return epic

    def delete_epic(self, id_project, id_epic):
        current_url = self.endPoint.format(id_project) + "/" + id_epic
        response = self.request_handler.delete_request(endpoint=current_url)
        return response.status_code

    def get_epic_schema(self):
        return StringHandler.convert_string_to_json(FileReader.get_file_content(self.__epic_schema_path))

    def delete_all_epics(self):
        self.get_epics()
        for epic in self.epics.values():
            url = self.__epic + "/" + str(epic)
            logger.info("Deleting %s" % url)
            self.request_handler.delete_request(endpoint=url)
