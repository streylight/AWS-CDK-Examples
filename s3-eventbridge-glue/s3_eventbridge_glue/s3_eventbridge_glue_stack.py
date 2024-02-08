from aws_cdk import (
    # Duration,
    Stack,
    aws_glue as glue
)
from constructs import Construct

class S3EventbridgeGlueStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        glue.CfnTrigger(
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
