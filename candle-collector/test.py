import schedule
import time

import datetime as dt
from mongoengine import *

import requests
import pymongo

from marshmallow import Schema, fields, pprint

class Candle1m(Document):
    timestamp = DateTimeField(required=True, unique=True)
    symbol = StringField(required=True)
    open = IntField()
    high = IntField()
    low = IntField(required=True)
    close = IntField(required=True)
    trades = IntField()
    volume = IntField()
    meta = {'collection': 'candles1m'}


connection = connect(db='market_data')
candles = Candle1m.objects().order_by('-timestamp')[:3]
low_list = [float(candle.low) for candle in candles]
timestamp_list = [str(candle.timestamp) for candle in candles]
print(low_list)
print(timestamp_list)
