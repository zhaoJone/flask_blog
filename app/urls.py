from settings import app
from views import user

app.add_url_rule('/', view_func=user.index)
app.add_url_rule('/users', view_func=user.UserApi.as_view('user'))
app.add_url_rule('/users/<int:user_id>', view_func=user.UserItemApi.as_view('userItem'))
