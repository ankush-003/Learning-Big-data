#!/usr/bin/env python3

import sys
import json

from kafka import KafkaConsumer

servers:list[str] = ['localhost:9092']

topic = sys.argv[1]

def deserialiser(value):
    # print(type(value))
    return json.loads(value.decode('utf-8'))

consumer = KafkaConsumer(topic, bootstrap_servers=servers, value_deserializer=deserialiser)

comments_data = {}

def getComments(user:str, comment:str, comments_data:dict):
    if user in comments_data:
        comments_data[user].append(comment)
    else:
        comments_data[user] = [comment]

for message in consumer:
    current_data = message.value
    eof = current_data.get("EOF", None)
    if(eof is not None):
        break
    receiver = current_data.get("posted_by", None)
    comment = current_data.get("comment", None)

    # print(receiver, comment)
    if receiver and comment:
        getComments(receiver, comment, comments_data)

print(json.dumps(dict(sorted(comments_data.items())), indent=4))
