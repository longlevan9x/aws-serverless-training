import boto3
from botocore.exceptions import ClientError

client = boto3.client("sqs")

def create_queue(name, attributes=None):
    """
    Creates an Amazon SQS queue.

    :param name: The name of the queue. This is part of the URL assigned to the queue.
    :param attributes: The attributes of the queue, such as maximum message size or
                       whether it's a FIFO queue.
    :return: A Queue object that contains metadata about the queue and that can be used
             to perform queue operations like sending and receiving messages.
    """
    if not attributes:
        attributes = {}

    try:
        queue = client.create_queue(QueueName=name, Attributes=attributes)
        print(queue)
        print("Created queue '%s' with URL=%s" % (name, queue["QueueUrl"]))
    except ClientError as error:
        print("Couldn't create queue named '%s'." % name)
        raise error
    else:
        return queue

def list_queues():
    response = client.list_queues()
    QueueUrls = response["QueueUrls"] 
    for QueueUrl in QueueUrls:
        print(QueueUrl)
        send_message(QueueUrl)
    # print(response)

def send_message(QueueUrl):
    response = client.send_message(
        QueueUrl=QueueUrl,
        MessageBody='Hello abcxyz %s' % QueueUrl,
        # DelaySeconds=123,
        MessageAttributes={
            'Test': {
                'StringValue': 'string',
                'DataType': 'String'
            }
        },
        # MessageSystemAttributes={
        #     'String': {
        #         'StringValue': 'string',
        #         'DataType': 'String'
        #     }
        # },
        # MessageDeduplicationId='string',
        # MessageGroupId='string'
    )

    print(response)

if __name__ == "__main__":
    # create_queue("TestCreateFromClient")
    list_queues()