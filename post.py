from peewee import *
import datetime

db = PostgresqlDatabase(
    'power_db',
    host = 'localhost',
    port = '5432',
    user = 'airan',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class MyUser(BaseModel):
    username = CharField(max_length=255, null=False, unique=True)
    email = CharField(max_length=255)
    age = IntegerField()


class Post(BaseModel):
    author = ForeignKeyField(MyUser, on_delete='CASCADE')
    title = CharField()
    date = DateField(default=datetime.datetime.now)


def post_create():
    post_author = int(input('Введите id пользователя: '))
    post_title = input('Введите текст поста: ')
    Post.create(
        author = post_author,
        title = post_title,
    )
