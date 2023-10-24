#!/usr/bin/env python3
import sys
import json

from kafka import KafkaConsumer

servers:list[str] = ['localhost:9092']

topic = sys.argv[2]

def deserialiser(value):
    # print(type(value))
    return json.loads(value.decode('utf-8'))

consumer = KafkaConsumer(topic, bootstrap_servers=servers, value_deserializer=deserialiser)

likes_data = {}

def getLikes(user:str, post_id:str, likes_data:dict):
    if user in likes_data:
        if post_id in likes_data[user]:
            likes_data[user][post_id] += 1
        else:
            likes_data[user][post_id] = 1
    else:
        likes_data[user] = {post_id: 1}

for message in consumer:
    data = message.value

    eof = data.get('EOF', None)
    if(eof is not None): break

    posted_by = data.get('posted_by', None)
    post_id = data.get('post_id', None)

    if posted_by and post_id:
        getLikes(posted_by, post_id, likes_data)

# sorting posts of a user
for user in likes_data.keys():
    likes_data[user] = dict(sorted(likes_data[user].items()))

print(json.dumps(dict(sorted(likes_data.items())), indent=4))
