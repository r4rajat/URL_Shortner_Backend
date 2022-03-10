from fastapi import FastAPI
import memcache
import os
import constant
from pymongo import MongoClient


# FastAPI Application Configuration
app = FastAPI()
# Memcached Client Configuration
MEMCACHED_HOST = os.environ.get(constant.MEMCACHED_HOST, '0.0.0.0')
MEMCACHED_PORT = os.environ.get(constant.MEMCACHED_PORT, '11211')
MEMCACHED_URL = MEMCACHED_HOST + ':' + MEMCACHED_PORT
memcache_client = memcache.Client([MEMCACHED_URL], debug=0)     # Memcached Connection
# MongoDB Configurations
MONGODB_HOST = os.environ.get(constant.MONGODB_HOST, '0.0.0.0')
MONGODB_PORT = os.environ.get(constant.MONGODB_PORT, '27017')
MONGODB_URL = 'mongodb://' + MONGODB_HOST + ':' + MONGODB_PORT
mongodb_client = MongoClient(MONGODB_URL)   # MongoDB Connection
db = mongodb_client['infracloud_db']    # Setting Database to Use
collection = db['url_shortner']     # Setting Collection to Use
