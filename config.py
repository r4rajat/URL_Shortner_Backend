from fastapi import FastAPI
import memcache
import os
import constant


# FastAPI Application Configuration
app = FastAPI()
# Memcached Client Configuration
MEMCACHED_HOST = os.environ.get(constant.MEMCACHED_HOST, 'localhost')
MEMCACHED_PORT = os.environ.get(constant.MEMCACHED_PORT, '11211')
MEMCACHED_SERVER = MEMCACHED_HOST + ':' + MEMCACHED_PORT
memcache_client = memcache.Client([MEMCACHED_SERVER], debug=0)
