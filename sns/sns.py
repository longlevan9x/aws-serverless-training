import boto3
import json
client = boto3.client('sns')

def list_topics(index):
    response = client.list_topics()
    # print(json.dumps(response))
    Topics = response["Topics"]

    for topic in Topics:
        publish(topic["TopicArn"], index)

def publish(TopicArn, index):
    Message = 'Hello from client %s' % index 
    response = client.publish(
        TopicArn=TopicArn,
        Message=Message,
        Subject='Subject from client',
        MessageStructure='string',
        MessageAttributes={
            "Test": {
              "DataType": "String",
              "StringValue": "TestString"
            }
        }
    )

    print(json.dumps(response))

if __name__ == '__main__':
    for i in range(10):
        list_topics(i)
        print(i)