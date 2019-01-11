# import time

from behave import Given, then, step

from src.pivotal_api_services.workspaces import WorkspacesServices
from src.utils.json_schema_validator import validate_json_schema

workspaces_services = WorkspacesServices()


@Given(u"I create workspaces")
def create_workspaces_step(context):
    data = {"name": "Workspace3"}
    context.workspaces_status, context.project_response = workspaces_services.create_workspace(data)


@step("I get a workspace")
def get_workspaces_step(context):
    workspaces_services.get_workspace(id=context.workspace_response["id"])


@step("I update the workspace")
def update_workspaces_step(context):
    data = {}
    for row in context.table:
        data = {"name": str(row['name'])}
    context.workspace_status, context.workspace_response = workspaces_services.update_workspace(
        id=str(context.workspace_response["id"]), data=data)


@step("I delete the workspace")
def update_workspaces_step(context):
    context.workspace_status = workspaces_services.delete_workspace(id=str(context.workspace_response["id"]))


# @then(u'I verify workspaces creation status is {status_code}')
# def step_impl(context, status_code):
#   print(context.workspaces_status)
#  assert context.workspaces_status == status_code, "Workspaces creation status is %s" % status_code


@step(u'I verify workspaces schema')
def step_impl(context):
    actual_response = workspaces_services.get_workspaces(id=str(context.workspaces_response["id"]))
    schema = workspaces_services.get_workspaces_schema()
    schema_failure_reason, is_schema_valid = validate_json_schema(schema, actual_response)
    assert is_schema_valid, "Workspaces Schema failed due to: {}".format(schema_failure_reason)
