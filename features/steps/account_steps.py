<<<<<<< HEAD
from behave import Given, Then, step

=======
#import time

from behave import Given, then, when
>>>>>>> 99a38f6f5fb6c3de2b732264aebe6840820bf598
from src.pivotal_api_services.accounts import AccountServices
from src.utils.json_schema_validator import validate_json_schema

account_services = AccountServices()


@Given(u"I create an account")
def create_account_step(context):
    data = {"account%5Bname%5D": "AccoBBB"}
    context.account_status, context.project_response = account_services.create_account(data)


@Then(u'I verify account creation status is {status_code}')
def step_impl(context, status_code):
    print(context.account_status)
    assert context.account_status == int(status_code), "Account creation status is %s" % status_code


@step(u'I verify account schema')
def step_impl(context):
    actual_response = account_services.get_account(id=str(context.account_response["id"]))
    schema = account_services.get_account_schema()
    schema_failure_reason, is_schema_valid = validate_json_schema(schema, actual_response)
    assert is_schema_valid, "Account Schema failed due to: {}".format(schema_failure_reason)
