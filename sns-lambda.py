import json

print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print(event["Records"])
    Record = event["Records"][0]
    Sns = Record["Sns"]
    Subject = Sns["Subject"]
    Message = Sns["Message"]
    print("Subject", Subject)
    print("Message", Message)
    return "Hello from lambda"  # Echo back the first key value
    #raise Exception('Something went wrong')
