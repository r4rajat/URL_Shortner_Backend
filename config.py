from fastapi import FastAPI
import memcache
import os
import constant
import pymongo


# FastAPI Application Configuration
app = FastAPI()
# Memcached Client Configuration
MEMCACHED_HOST = os.environ.get(constant.MEMCACHED_HOST, 'localhost')
MEMCACHED_PORT = os.environ.get(constant.MEMCACHED_PORT, '11211')
MEMCACHED_URL = MEMCACHED_HOST + ':' + MEMCACHED_PORT
memcache_client = memcache.Client([MEMCACHED_URL], debug=0)     # Memcached Connection
# MongoDB Configurations
MONGODB_HOST = os.environ.get(constant.MONGODB_HOST, 'localhost')
MONGODB_PORT = os.environ.get(constant.MONGODB_PORT, '27017')
MONGODB_URL = 'mongodb://' + MONGODB_HOST + ':' + MONGODB_PORT
MONGODB_DB = os.environ.get(constant.MONGODB_DB, 'infracloud_db')
MONGODB_COLLECTION = os.environ.get(constant.MONGODB_COLLECTION, 'url_shortner')
try:
    mongodb_client = pymongo.MongoClient(MONGODB_URL)   # MongoDB Connection
    db = mongodb_client[MONGODB_DB]    # Setting Database to Use
    collection = db[MONGODB_COLLECTION]     # Setting Collection to Use
except pymongo.errors.ConnectionError as e:
    raise Exception(e)


from apis import url_shortener