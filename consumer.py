from aiokafka import AIOKafkaConsumer
import logging
import os
import asyncio

loop = asyncio.get_event_loop()

logging.basicConfig(level=logging.INFO)

TOPIC = os.environ.get("KAFKA_TOPIC", "vulnerabilities-qa")
KAFKA_GROUP = os.environ.get("KAFKA_GROUP", "vulnerabilities")
BOOTSTRAP_SERVERS = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

async def consume():
    consumer = AIOKafkaConsumer(
        TOPIC,
        loop=loop, bootstrap_servers=BOOTSTRAP_SERVERS,
        group_id=KAFKA_GROUP)
    # Get cluster layout and join group `my-group`
    await consumer.start()
    print("consumer has started:")
    print("TOPIC:", TOPIC)
    print("KAFKA_GROUP:", KAFKA_GROUP)
    print("BOOTSTRAP_SERVERS:", BOOTSTRAP_SERVERS)
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, msg.value, msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

loop.run_until_complete(consume())
