import time

from behave import Given, then, step

from src.pivotal_api_services.projects import ProjectServices
from src.utils.json_schema_validator import validate_json_schema

project_services = ProjectServices()


@Given(u"I create a project")
def create_project_step(context):
    data = {"name": "New Project"+ str(time.time())}
    context.project_status, context.project_response = project_services.create_project(data)


@step("I update the project")
def update_project_step(context):
    data = {}
    for row in context.table:
        data = {"name": str(row['name'])}
    context.project_status, context.project_response = project_services.update_project(
        id=str(context.project_response["id"]), data=data)


@step("I delete the project")
def update_project_step(context):
    context.project_status = project_services.delete_project(id=str(context.project_response["id"]))


@then('I verify project updated status is {status_code}')
def step_impl(context, status_code):
    print(context.project_status)
    assert context.project_status == int(status_code), "Project updated status is %s" % status_code


@then(u'I verify project creation status is {status_code}')
def step_impl(context, status_code):
    print(context.project_status)
    assert context.project_status == int(status_code), "Project creation status is %s" % status_code
    print 'the project was created because the respone status is '+ str(context.project_status)


@then('I verify project deleted status is {status_code}')
def step_impl(context, status_code):
    print(context.project_status)
    assert context.project_status == int(status_code), "Project deleted status is %s" % status_code


@step(u'I verify project schema')
def step_impl(context):
    actual_response = project_services.get_project(id=str(context.project_response["id"]))
    schema = project_services.get_project_schema()
    schema_failure_reason, is_schema_valid = validate_json_schema(schema, actual_response)
    assert is_schema_valid, "Project Schema failed due to: {}".format(schema_failure_reason)