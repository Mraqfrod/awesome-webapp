from www.orm import Model, IntegerField, StringField


class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key=True)
    name = StringField()

user = User(id=123, name='Michael')
user.save()