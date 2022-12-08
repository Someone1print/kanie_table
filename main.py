from peewee import *
import datetime
from post import post_create

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


db.create_tables([MyUser, Post])

user = input('Введите имя пользователя: ')
user_email = input('Введите email пользователя: ')
user_age = int(input('Введите возраст пользователя: '))

MyUser.create(
    username = user,
    email = user_email,
    age = user_age
)

# post_author = int(input('Введите id пользователя: '))
# post_title = input('Введите текст поста: ')
print('Теперь пост')

post_create()


# user = MyUser.select().where(MyUser.username=='Eva') 
# rows = Post.select().where(Post.author==user) 
 
# for row in rows: 
#     print(f'author:{row.author}, title: {row.title}')


db.close()