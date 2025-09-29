from django.contrib.auth.models import User
from ninja import ModelSchema


class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]
