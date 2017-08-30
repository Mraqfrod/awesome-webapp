from www.orm import Model, IntegerField, StringField


class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key=True)
    name = StringField()

