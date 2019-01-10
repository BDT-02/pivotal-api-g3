from behave import  then, step

from src.pivotal_api_services.epics import EpicServices
from src.utils.json_schema_validator import validate_json_schema

epic_services = EpicServices()


@step(u"I create a epic")
def create_epic_step(context):

    data = {}
    for row in context.table:
        data = {"name": str(row['label'])}
    context.epic_status, context.epic_response = epic_services.create_epic(
        id_project=str(context.project_response["id"]), data=data)


@step(u"I update a epic")
def update_epic_step(context):
    data = {}
    for row in context.table:
        data = {"name": str(row['label'])}
    context.epic_status, context.epic_response = epic_services.update_epic(
        id_project=str(context.project_response["id"]), id_epic=str(context.epic_response["id"]), data=data)


@step(u"I delete the epic")
def update_project_step(context):
    context.epic_status = epic_services.delete_epic(id_project=str(context.project_response["id"]),
                                                    id_epic=str(context.epic_response["id"]))


@then(u'I verify epic updated status is {status_code}')
def step_impl(context, status_code):
    print(context.epic_status)
    assert context.epic_status == int(status_code), "epic creation status is %s" % status_code
    # print 'the epic was updated because the response status is ' + str(context.epic_status) + ' '


@then(u'I verify epic created status is {status_code}')
def step_impl(context, status_code):
    print(context.epic_status)
    assert context.epic_status == int(status_code), "Epic creation status is %s" % status_code


@then(u'I verify epic deleted status is {status_code}')
def step_impl(context, status_code):
    print(context.epic_status)
    assert context.epic_status == int(status_code), "epic deleted status is %s" % status_code


@step(u'I verify epic schema')
def step_impl(context):
    actual_response = epic_services.get_epic(id_project=str(context.project_response["id"]),
                                             id_epic=str(context.epic_response["id"]))
    schema = epic_services.get_epic_schema()
    schema_failure_reason, is_schema_valid = validate_json_schema(schema, actual_response)
    assert is_schema_valid, "Project Schema failed due to: {}".format(schema_failure_reason)

