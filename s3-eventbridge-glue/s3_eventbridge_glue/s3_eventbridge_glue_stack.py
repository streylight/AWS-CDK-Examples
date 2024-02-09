from aws_cdk import (
    # Duration,
    Stack,
    aws_glue as glue,
    aws_s3 as s3
)

import aws_cdk as cdk
from constructs import Construct

class S3EventbridgeGlueStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self, 
            "GlueDestinationBucket",
            versioned=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True)
        
        tigger = glue.CfnTrigger(
            self,
            "MyETLTrigger",
            type="ON_DEMAND",
            actions=[
                {
                    "jobName": "MyETLJob",
                    "arguments": {
                        "--job-language": "python",
                        "--job-bookmark-option": "job-bookmark-enable"
                    },
                },
            ])
