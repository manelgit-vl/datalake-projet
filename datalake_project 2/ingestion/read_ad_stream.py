from kafka import KafkaConsumer
import json
import os
from datetime import datetime

consumer = KafkaConsumer(
    'ad_stream',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

os.makedirs("Data_lake/raw/ad_stream", exist_ok=True)

for message in consumer:
    data = message.value
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    filename = f"Data_lake/raw/ad_stream/ad_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"Saved {filename}")
