#import time

from behave import Given, then, step

from src.pivotal_api_services.accounts import AccountServices
from src.utils.json_schema_validator import validate_json_schema

workspaces_services = AccountServices()


@Given(u"I create a workspaces")
def create_workspaces_step(context):
    data = {"name": "WorkspaceVZ"}
    context.workspaces_status, context.project_response = workspaces_services.create_workspaces(data)



@then(u'I verify account creation status is {status_code}')
def step_impl(context, status_code):
    print(context.account_status)
    assert context.account_status == status_code, "Account creation status is %s" % status_code


@step(u'I verify account schema')
def step_impl(context):
    actual_response = account_services.get_account(id=str(context.account_response["id"]))
    schema = account_services.get_account_schema()
    schema_failure_reason, is_schema_valid = validate_json_schema(schema, actual_response)
    assert is_schema_valid, "Account Schema failed due to: {}".format(schema_failure_reason)
