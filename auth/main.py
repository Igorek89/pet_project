import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

import config

app = FastAPI(
    title=config.config.project_name,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


# configure_jwt(app)
# register_error_handlers(app)


app.include_router(event_handler.router, prefix='/api/v1/', tags=['events'])


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
    )
