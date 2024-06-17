import boto3
import json
import logging

TABLE_NAME = 'visitors'
KEY_NAME = 'emma-cv'

client = boto3.client('dynamodb')

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

def lambda_handler(event, context):
    try:
        GetItem = client.get_item(
            TableName=TABLE_NAME,
            Key={KEY_NAME: {'S': KEY_NAME}}
        )
    except Exception as e:
        logger.error(f"Error getting item: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'An error occurred while getting the visitor count'})
        }

    current_visitors = GetItem.get('Item', {}).get('visitors', {}).get('N', '0')
    new_visitors = int(current_visitors) + 1

    try:
        client.update_item(
            TableName=TABLE_NAME,
            Key={KEY_NAME: {'S': KEY_NAME}},
            UpdateExpression='SET visitors = :val1',
            ExpressionAttributeValues={
                ':val1': {'N': str(new_visitors)}
            }
        )
    except Exception as e:
        logger.error(f"Error updating item: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'An error occurred while updating the visitor count'})
        }

    response = {
        'statusCode': 200,
        'body': json.dumps({'new_visitors': new_visitors})
    }

    return response
