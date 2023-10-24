#!/usr/bin/env python 3

import sys
import json

from kafka import KafkaConsumer

servers:list[str] = ['localhost:9092']

comments, likes, shares = sys.argv[1:]

def deserialiser(value):
    # print(type(value))
    return json.loads(value.decode('utf-8'))

consumer = KafkaConsumer(bootstrap_servers=servers, value_deserializer=deserialiser)
consumer.subscribe([comments, likes, shares])

eof_count = 0

users_data = {}

def getLikes(user:str, users_data:dict):
    if user in users_data:
        if 'likes' in users_data[user]:
            users_data[user]['likes'] += 1
        else:
            users_data[user]['likes'] = 1
    else:
        users_data[user] = {'likes': 1}

def getComments(user:str, users_data:dict):
    if user in users_data:
        if 'comments' in users_data[user]:
            users_data[user]['comments'] += 1
        else:
            users_data[user]['comments'] = 1
    else:
        users_data[user] = {'comments': 1}

def getShares(user:str, shared_num:int, users_data:dict):
    if user in users_data:
        if 'shares' in users_data[user]:
            users_data[user]['shares'] += shared_num
        else:
            users_data[user]['shares'] = shared_num
    else:
        users_data[user] = {'shares': shared_num}

for message in consumer:
    data = message.value

    if(data.get('EOF', None)): eof_count+= 1
    if(eof_count == 3): break

    user = data.get('posted_by', None)
    if(user):
        if(message.topic == comments):
            getComments(user, users_data)
        elif (message.topic == likes):
            getLikes(user, users_data)
        elif (message.topic == shares):
            shared_num = len(data.get('shared_to', None)) if data.get('shared_to', None) else 0
            getShares(user, shared_num, users_data)
        else:
            print("Invalid Topic")
            continue

# print(users_data)

popularity_data = {}

def getPopularity(user:str, comments:int, likes:int, shares:int, popularity_data:dict):
    popularity = round((likes + 20 * shares + 5 * comments) / 1000, 3)
    popularity_data[user] = popularity

for user in users_data.keys():
    getPopularity(user, users_data[user].get('comments', 0), users_data[user].get('likes', 0), users_data[user].get('shares', 0), popularity_data)

print(json.dumps(dict(sorted(popularity_data.items())), indent=4))
