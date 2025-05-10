from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

ads = [
    {"campaign_id": 1, "ad_type": "banner", "clicks": 120},
    {"campaign_id": 2, "ad_type": "video", "clicks": 85},
    {"campaign_id": 3, "ad_type": "popup", "clicks": 42}
]

while True:
    ad = random.choice(ads)
    producer.send('ad_stream', ad)
    print("Sent:", ad)
    time.sleep(2)
