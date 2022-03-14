from config import app
import constant
from fastapi.responses import JSONResponse
from fastapi import BackgroundTasks
from pydantic import BaseModel
from typing import Optional
from apis.service_funcs import find_one, insert_one, get_data_from_memcached, set_data_in_memcached, create_short_url


class Payload(BaseModel):
    long_url: str
    preferred_short_url: Optional[str] = None


def _set_data_to_db_memcached(long_url: str, short_url: str):
    try:
        document = {
            constant.LONG_URL: long_url,
            constant.SHORT_URL: short_url
        }
        insert_one(document=document)
        set_data_in_memcached(key=long_url, value=short_url)

    except Exception as e:
        raise Exception(e)


@app.get('/get-shortened-url')
async def get_shortened_url(long_url: str):
    """ Get Already Shortened URL for the Long URL """
    try:
        # Splitting URL to just get URL in format www.xyz.com
        long_url = long_url.split('//')
        long_url.reverse()
        long_url = long_url[0]
        short_url = get_data_from_memcached(key=long_url)
        if short_url:
            content = {
                constant.MESSAGE: "Short URL Found for " + long_url,
                constant.SHORT_URL: "if.cld/" + short_url
            }
            headers = {
                constant.FROM: "Memcached"
            }
            return JSONResponse(content=content, status_code=200, headers=headers)

        else:
            data = find_one({constant.LONG_URL: long_url})
            if data:
                short_url = data[constant.SHORT_URL]
                content = {
                    constant.MESSAGE: "Short URL Found for " + long_url,
                    constant.SHORT_URL: "if.cld/" + short_url
                }
                headers = {
                    constant.FROM: "MongoDB"
                }
                return JSONResponse(content=content, status_code=200, headers=headers)
            else:
                content = {
                    constant.MESSAGE: "No Shortened URL found for " + long_url
                }
                return JSONResponse(content=content, status_code=404)

    except Exception as e:
        content = {
            constant.ERROR: "Error Occurred",
            constant.CAUSE: str(e)
        }
        return JSONResponse(content=content, status_code=500)


@app.post('/create-shortened-url')
async def create_shortened_url(payload: Payload, background_task: BackgroundTasks):
    """ Creates Shortened URLs for the Long URLs """
    try:
        long_url = payload.long_url
        preferred_short_url = payload.preferred_short_url
        long_url = long_url.split('//')
        long_url.reverse()
        long_url = long_url[0]
        short_url, status = create_short_url(long_url=long_url, preferred_short_url=preferred_short_url)
        if status == 201:
            background_task.add_task(_set_data_to_db_memcached, long_url, short_url)
            if preferred_short_url:
                if short_url != preferred_short_url:
                    content = {
                        constant.MESSAGE: "Couldn't create Preferred Short URL for " + long_url + "as it already exists "
                                                                                                  "in our systems",
                        constant.SHORT_URL: "if.cld/" + short_url
                    }
                    return JSONResponse(content=content, status_code=201)
                else:
                    content = {
                        constant.MESSAGE: "Short URL created for " + long_url,
                        constant.SHORT_URL: "if.cld/" + short_url
                    }
                    return JSONResponse(content=content, status_code=201)
            else:
                content = {
                    constant.MESSAGE: "Short URL created for " + long_url,
                    constant.SHORT_URL: "if.cld/" + short_url
                }
                return JSONResponse(content=content, status_code=201)
        else:
            content = {
                constant.MESSAGE: "Short URL already there for " + long_url,
                constant.SHORT_URL: "if.cld/" + short_url
            }
            return JSONResponse(content=content, status_code=409)

    except Exception as e:
        content = {
            constant.ERROR: "Error Occurred",
            constant.CAUSE: str(e)
        }
        return JSONResponse(content=content, status_code=500)
