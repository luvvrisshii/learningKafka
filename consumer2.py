from confluent_kafka import Consumer, KafkaException, KafkaError

# Configure the Kafka consumer
conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "my_group",
    'auto.offset.reset': 'earliest'
}

# Create Consumer instance
consumer = Consumer(conf)

# Subscribe to topics
topics = ['prod_user']
consumer.subscribe(topics)

# Poll for new messages
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print('%% %s [%d] reached end at offset %d\n' %
                      (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # Message received
            print('Consumer 2 received message: {} from topic: {}'.format(msg.value().decode('utf-8'), msg.topic()))
except KeyboardInterrupt:
    pass
finally:
    # Close the consumer
    consumer.close()
