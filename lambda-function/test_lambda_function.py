import os
os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
os.environ['AWS_SECURITY_TOKEN'] = 'testing'
os.environ['AWS_SESSION_TOKEN'] = 'testing'
os.environ['AWS_DEFAULT_REGION'] = 'us-west-2'
import boto3
from moto import mock_aws
import json
from lambda_function import lambda_handler



@mock_aws
def test_lambda_handler():
    # Set up the mock DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='visitors',
        KeySchema=[{'AttributeName': 'emma-cv', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'emma-cv', 'AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )
    table.put_item(Item={'emma-cv': 'emma-cv', 'visitors': 10})

    # Call the lambda function
    response = lambda_handler({}, {})

    # Parse the JSON string into a dictionary
    body = json.loads(response['body'])

    # Check the response
    assert response['statusCode'] == 200
    assert body['new_visitors'] == 11
