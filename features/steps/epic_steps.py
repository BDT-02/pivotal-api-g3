import time

from behave import Given, then, step

from src.pivotal_api_services.epic import EpicServices
from src.utils.json_schema_validator import validate_json_schema

epic_services = EpicServices()


@Given(u"I update an epic")
def update_epic_step(context):
    data = {"name": "New epic" + str(time.time())}
    context.epic_status, context.epic_response = epic_services.update_epic(data)


@then(u'I verify epic creation status is {status_code}')
def step_impl(context, status_code):
    print(context.epic_status)
    assert context.epic_status == int(status_code), "epic creation status is %s" % status_code
    print 'the epic was created because the response status is ' + str(context.epic_status)


@step(u'I verify epic schema')
def step_impl(context):
    actual_response = epic_services.get_epic(id=str(context.epic_response["id"]))
    schema = epic_services.get_epic_schema()
    schema_failure_reason, is_schema_valid = validate_json_schema(schema, actual_response)
    assert is_schema_valid, "epic Schema failed due to: {}".format(schema_failure_reason)
