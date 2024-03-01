import aws_cdk as core
import aws_cdk.assertions as assertions

from organizations_create_accounts.organizations_create_accounts_stack import OrganizationsCreateAccountsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in organizations_create_accounts/organizations_create_accounts_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = OrganizationsCreateAccountsStack(app, "organizations-create-accounts")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
