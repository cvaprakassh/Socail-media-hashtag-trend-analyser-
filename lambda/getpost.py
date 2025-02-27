import json
import boto3

def lambda_handler(event, context):
     dynamodb = boto3.resource('dynamodb')
     table = dynamodb.Table('tb_post')
     response = table.scan()
     items = response['Items']
     return {
            'statusCode': 200,
            'body': json.dumps(items)
        }

