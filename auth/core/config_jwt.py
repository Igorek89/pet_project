from fastapi import FastAPI
from async_fastapi_jwt_auth import AuthJWT
from async_fastapi_jwt_auth.exceptions import AuthJWTException


def configure_jwt(app: FastAPI) ->
