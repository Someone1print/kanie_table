from peewee import *
import datetime

db = PostgresqlDatabase(
    'car_db',
    host = 'localhost',
    port = '5432',
    user = 'sto',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Batia(BaseModel):
    username = CharField(max_length=255, null=False, unique=True)


class Car(BaseModel):
    author = ForeignKeyField(Batia, on_delete='CASCADE')
    car = CharField()
    date = DateField(default=datetime.datetime.now)


db.create_tables([Batia, Car])

# Batia.create(
#     username = 'Dima'
# )

# Batia.create(
#     username = 'Fedor'
# )

# Batia.create(
#     username = 'Edik'
# )

# Batia.create(
#     username = 'Vovan'
# )

# Batia.create(
#     username = 'Anatolii'
# )

# Car.create(
#     author = 1,
#     car = 'Bmw',
# )

# Car.create(
#     author = 1,
#     car = 'Mercedes-Benz',
# )

# Car.create(
#     author = 2,
#     car = 'Volvo cx 60',
# )

# Car.create(
#     author = 2,
#     car = 'Audi r8',
# )

# Car.create(
#     author = 3,
#     car = 'Lada priora'
# )

# Car.create(
#     author = 3,
#     car = 'Moskvich 2109'
# )

# Car.create(
#     author = 4,
#     car = 'McLaren siena',
# )

# Car.create(
#     author = 4,
#     car = 'Telsa model x'
# )

# Car.create(
#     author = 5,
#     car = 'Rino logon' 
# )

# Car.create(
#     author = 5,
#     car = 'Lamborghini huracan'
# )


db.close()