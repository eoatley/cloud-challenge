import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    GetItem = client.get_item(
        TableName='visitors',
        Key={
            'emma-cv': {'S': 'emma-cv'}
        }
    )

    current_visitors = GetItem.get('Item', {}).get('visitors', {}).get('N', '0')

    new_visitors = int(current_visitors)+1

    client.update_item(
        TableName='visitors',
        Key={
            'emma-cv': {'S': 'emma-cv'}
        },
        UpdateExpression='SET visitors = :val1',
        ExpressionAttributeValues={
            ':val1': {'N': str(new_visitors)}
        }
    )

    response = {
        'statusCode': 200,
        'body': new_visitors
    }

    return response
