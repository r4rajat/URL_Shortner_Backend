import constant
from config import collection, memcache_client
import random
import string


def find_one(fields):
    try:
        data = collection.find_one(fields)
        return data
    except Exception as e:
        raise Exception(e)


def insert_one(document):
    try:
        data = collection.insert_one(document)
        return data
    except Exception as e:
        raise Exception(e)


def get_data_from_memcached(key):
    try:
        value = memcache_client.get(key)
        return value
    except Exception as e:
        raise Exception(e)


def set_data_in_memcached(key, value):
    try:
        status = memcache_client.set(key, value)
        return status
    except Exception as e:
        raise Exception(e)


def create_short_url(long_url, preferred_short_url):
    try:
        short_url = get_data_from_memcached(key=long_url)
        if short_url:
            return short_url, 409
        short_url = find_one({constant.LONG_URL: long_url})
        if short_url:
            return short_url[constant.SHORT_URL], 409
        else:
            if preferred_short_url:
                preferred_url_exists = find_one({constant.SHORT_URL: preferred_short_url})
                if not preferred_url_exists:
                    short_url = preferred_short_url
                    return short_url, 201
            chars = string.ascii_letters + string.digits
            length = 6
            short_url = ''.join(random.choice(chars) for _ in range(length))
            return short_url, 201
    except Exception as e:
        raise Exception(e)


def get_long_url_func(short_url):
    try:
        long_url = find_one({constant.SHORT_URL: short_url})
        long_url = long_url[constant.LONG_URL]
        return long_url

    except Exception as e:
        raise Exception(e)