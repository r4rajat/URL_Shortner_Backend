import uvicorn
import os
import constant


if __name__ == '__main__':
    ENVIRONMENT_RELOAD = os.environ.get(constant.APP_RELOAD, True)
    ENVIRONMENT_HOST = os.environ.get(constant.APP_HOST, '0.0.0.0')
    ENVIRONMENT_PORT = int(os.environ.get(constant.APP_PORT, '5000'))
    ENVIRONMENT_WORKERS = int(os.environ.get(constant.APP_WORKERS, '1'))
    uvicorn.run(app='config:app', reload=ENVIRONMENT_RELOAD, host=ENVIRONMENT_HOST, port=ENVIRONMENT_PORT,
                workers=ENVIRONMENT_WORKERS)
