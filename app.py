#!/usr/bin/env python3

import aws_cdk as cdk

from sqs_lambda_cdk_demo.sqs_lambda_cdk_demo_stack import SqsLambdaCdkDemoStack


app = cdk.App()
SqsLambdaCdkDemoStack(app, "SqsLambdaCdkDemoStack")

app.synth()
