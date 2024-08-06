from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources,
)


class SqsLambdaCdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create SQS queue
        queue = sqs.Queue(
            self, "SqsLambdaCdkDemoQueue",
            visibility_timeout=Duration.seconds(300),
        )

        # Create Lambda function
        sqs_lambda = lambda_.Function(
            self,
            "SQSLambda",
            handler="lambda_handler.handler",
            runtime=lambda_.Runtime.PYTHON_3_10,
            code = lambda_.Code.from_asset("lambda"),
        )

        # Create event source for Lambda function
        sqs_event_soure = lambda_event_sources.SqsEventSource(queue)

        # Add event source to Lambda function
        sqs_lambda.add_event_source(sqs_event_soure)
                                      
