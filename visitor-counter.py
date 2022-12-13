import json
import boto3
def lambda_handler(event, context):

    # conn to DynamoDB resource
    client = boto3.resource('dynamodb')
    
    # create DynamoDB client to visitor_count table
    table = client.Table('visitor_count')
    
    # increment visitor_count for index.html
    # https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/persisting-data/dynamodb/step-3
    
    response = table.update_item(
        Key={
            'path': 'index.html'
        },
        AttributeUpdates={
            'visitor_count':{
                'Value':1,
                'Action': 'ADD'
            }
        }
    )
    
    # get visitor count from the visitor_count table for index.html
    response = table.get_item(
        Key={
            'path': 'index.html'
        }
    )
    visitor_count = (response['Item']['visitor_count'])
    
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': visitor_count
    }
