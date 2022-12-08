import requests
from peewee import *
import datetime


db = PostgresqlDatabase(
    'vest',
    host = 'localhost',
    port = '5432',
    user = 'kanie',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Kanie(BaseModel):
    title = CharField()
    kol_vo_bykv = CharField()
    sogl = IntegerField()
    glass = IntegerField()
    avg_word = IntegerField()
    long_word = CharField()
    date = DateField(default=datetime.datetime.now)


db.create_tables([Kanie])

p = 0
j = 0
k = 0
quete = []
quete.clear()
while p < 10:
    quete1 = []
    res = requests.get('https://api.kanye.rest/')

    a = res.json()
    for key, value in a.items():
        if value not in quete:
            quete.append(value)
            quete1.append(value)
            p += 1
            print(quete1)
            c = len([i for i in value if i.isalpha()])
            for bykva in value:
                if bykva in 'qwrtpdfghjklzxcvbnm':
                    j += 1
                if bykva in 'eyuioa':
                    k += 1
                else:
                    continue
            
            abv = value.split(' ')
            fg = len(abv)
            avg = c/fg

            f = max(abv, key=len)
            abv.remove(f)
            t = max(abv, key=len)
            abv.remove(t)
            m = max(abv, key=len)
            abv.remove(m)
            gh = t,f,m


    Kanie.create(
        title = quete1,
        kol_vo_bykv = c,
        sogl = j,
        glass = k,
        avg_word = avg,
        long_word = gh
    )


db.close()