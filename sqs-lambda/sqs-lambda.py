import json

def lambda_handler(event, context):
    Record = event["Records"][0]
    body = Record["body"]
    attributes = Record["attributes"]
    messageId = Record["messageId"]
    # print(json.dumps(event))
    print(body, messageId, attributes)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Lambda from client!')
    }
