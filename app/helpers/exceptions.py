import json

from werkzeug.exceptions import HTTPException

from .http_status import HTTP_200_OK


class BaseApiException(HTTPException):
    code = HTTP_200_OK
    customize_code = 20000
    customize_message = None

    def __init__(
            self,
            customize_code: int = None,
            code: int = None,
            customize_message: str = None,
            *opts,
            **kwargs):
        if code is not None:
            self.code = code
        if customize_code is not None:
            self.customize_code = customize_code
        if customize_message is not None:
            self.customize_message = customize_message
        super().__init__(description=self.message, *opts, **kwargs)

    @property
    def message(self):
        from .customize_status import CUSTOMIZE_STATUS_CODE

        message = CUSTOMIZE_STATUS_CODE.get(self.customize_code)

        if message is None and self.customize_message is not None:
            message = self.customize_message
        if message is None:
            message = 'Unknown Error'

        return message

    def get_body(self, environ=None):
        """Get the Json body."""
        response_structure = {'code': self.customize_code, 'messages': self.message}

        return json.dumps(response_structure)

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [("Content-Type", "application/json")]


class ServerError(BaseApiException):
    customize_code = 32000
    customize_message = '服务器繁忙'
