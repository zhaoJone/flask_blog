from werkzeug.exceptions import HTTPException
from marshmallow.exceptions import ValidationError

from settings import app
from helpers.exceptions import BaseApiException
import urls


@app.errorhandler(Exception)
def error_handler(e):
    if isinstance(e, ValidationError):
        return BaseApiException(code=400, customize_message=e.messages)
    if isinstance(e, BaseApiException):
        return e
    if isinstance(e, HTTPException):
        return BaseApiException(code=e.code, customize_message=e.description)
    if isinstance(e, Exception):
        print(e)
        return BaseApiException(code=500)


if __name__ == '__main__':
    app.run()
