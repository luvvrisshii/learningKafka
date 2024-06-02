from confluent_kafka.admin import AdminClient, NewTopic

# Configure the Kafka bootstrap servers
bootstrap_servers = "localhost:9092"

# Create AdminClient configuration
conf = {'bootstrap.servers': bootstrap_servers}

# Create AdminClient instance
admin_client = AdminClient(conf)

# Define topics to be created
new_topics = [
    NewTopic("test_user", num_partitions=3, replication_factor=1),
    NewTopic("prod_user", num_partitions=3, replication_factor=1)
]

# Create topics
admin_client.create_topics(new_topics)

# List topics
topics = admin_client.list_topics().topics
print("Current topics:", topics)

# Close AdminClient
