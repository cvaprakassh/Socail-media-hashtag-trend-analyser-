import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('tb_post')
    table.put_item(
        Item={
            'postid':event['postId'],
            'tags':event['tags'],
            'post_content':event['post_content']
        })
    return {
        'statusCode': 200,
        'body': json.dumps('Insert Post Invoked!')
    }
