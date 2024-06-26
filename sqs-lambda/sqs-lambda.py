# event brigde -> SNS -> SQS -> Lambda
import json

def lambda_handler(event, context):
    Record = event["Records"][0]
    body = Record["body"]
    attributes = Record["attributes"]
    messageId = Record["messageId"]

    print("messageId", messageId),
    print("attributes", attributes)

    if is_json(body):
        body = json.loads(body)

    if body and type(body) is dict and body["Type"] == "Notification":
        print("body sns", json.dumps(body))
        Subject = ""
        MessageAttributes = ""

        if "Subject" in body:
            #from sns
            Subject = body["Subject"]
        # else:
            #from event brigde

        if "MessageAttributes" in body:
            MessageAttributes = body["MessageAttributes"]

        Message = body["Message"]
        print("Subject", Subject)
        print("Message", Message)
        print("MessageAttributes", MessageAttributes)
    else:
        #for other
        print("body1", body)

    # print(json.dumps(event))
   
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Lambda from client!')
    }

def is_json(value):
    try:
        json.loads(value)
        return True
    except ValueError as e:
        return False
