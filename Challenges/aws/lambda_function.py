import json

def lambda_handler(event, context):
    def response(data, status_code=200):
        return {
            'statusCode': status_code,
            'body': json.dumps(data)            
        }