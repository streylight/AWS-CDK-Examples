from aws_cdk import (
    CfnTag,
    Stack,
    aws_organizations as Organizations,
)
from constructs import Construct

class OrganizationsCreateAccountsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        staging_account = Organizations.CfnAccount(self, 'DemoAppStagingAccount',
            email = '<your-email-address>',
            account_name = 'DemoAppStagingAccount',
            parent_ids = ['ou-8lvd-ftapv58n'],
            tags = [CfnTag(key='Name', value='DemoAppStagingAccount')]
        )
