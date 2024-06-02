from confluent_kafka import Producer
from time import sleep
from time import sleep

# Configure the Kafka producer
conf = {'bootstrap.servers': "localhost:9092"}

# Create Producer instance
producer = Producer(conf)


# Delivery report callback
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


# Produce messages to topic1 and topic2
topics = ['test_user', 'prod_user']

while True:


    for i in range(10):
        for topic in topics:
            producer.produce(topic, key=str(i), value='Hi! I am Kakfa', callback=delivery_report)
            producer.poll(0)

# Wait for any outstanding messages to be delivered and delivery report callbacks to be triggered
producer.flush()
