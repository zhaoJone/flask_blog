from flask.views import MethodView


class BaseView(MethodView):
    model = None
    schema = None
