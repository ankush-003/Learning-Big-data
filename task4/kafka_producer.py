#!/usr/bin/env python3

import sys
import json

from kafka import KafkaProducer

server:list[str] = ['localhost:9092']

def serialiser(message: dict):
    return json.dumps(message).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=server, value_serializer=serialiser)

comments, likes, shares = sys.argv[1:]

topic = None
message = None

def getMessage(msg_type: str, words: list[str]) -> tuple[str, dict]:
    if (msg_type == 'like'):
        topic = likes
        message = {'user_liking': words[0], 'posted_by': words[1], 'post_id': words[2]}

    elif (msg_type == 'share'):
        topic = shares
        message = {'user_sharing': words[0], 'posted_by': words[1], 'post_id': words[2], 'shared_to':words[3:]}

    elif (msg_type == 'comment'):
        topic = comments
        comment = " ".join(words[3:])
        message = {'user_commenting': words[0], 'posted_by': words[1], 'post_id': words[2], 'comment': comment[1:-1]}

    else: 
        topic, message = None, None

    return (topic, message)

for line in sys.stdin:
    words = line.strip().split()

    if 'EOF' in words:
        for topic in sys.argv[1:]:
            producer.send(topic, value={'EOF': True})
        break    

    topic, message = getMessage(words[0], words[1:])
    if(topic is None or message is None):
        print("Invalid data")
        continue

    # print(serialiser(message))
    producer.send(topic, value=message)

producer.close()    
