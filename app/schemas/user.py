from marshmallow import post_load

from settings import db, ma
from models.user import User


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    @post_load
    def make_instance(self, data, **kwargs):
        instance = User(**data)
        db.session.add(instance)
        db.session.commit()
        return instance
