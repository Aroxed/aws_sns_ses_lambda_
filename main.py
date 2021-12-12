import boto3


def create_topic(name):
    """
    Creates a notification topic.

    :param name: The name of the topic to create.
    :return: The newly created topic.
    """
    sns = boto3.resource("sns")
    topic = sns.create_topic(Name=name)
    return topic


def publish_message(topic, message):
    """
    Publishes a message to a topic.

    :param topic: The topic to publish to.
    :param message: The message to publish.
    :return: The ID of the message.
    """
    response = topic.publish(Message=message)
    message_id = response['MessageId']
    return message_id


topic = create_topic("learnaws-boto3-sns")
print(publish_message(topic, "This is my message!"))
