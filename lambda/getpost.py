import json
import boto3

def lambda_handler(event, context):
     dynamodb = boto3.resource('dynamodb')
     table = dynamodb.Table('tb_post')
     response = table.scan()
     data = response['Items']
     while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }

