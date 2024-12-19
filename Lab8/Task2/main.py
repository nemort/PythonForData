from peewee import *
from datetime import date, time

db = SqliteDatabase("orders.db")


class Couriers(Model):
    courierId = PrimaryKeyField()
    surname = TextField()
    name = TextField()
    patronymic = TextField()
    passportNumber = IntegerField()
    birthDate = DateField()
    employmentDate = DateField()
    workingDayStart = TimeField()
    workingDayEnd = TimeField()
    city = TextField()
    street = TextField()
    house = IntegerField()
    flat = IntegerField()
    phoneNumber = IntegerField()

    class Meta:
        database = db
        table_name = 'couriers'


class Vehicles(Model):
    vehicleId = PrimaryKeyField()
    brand = TextField()
    registrationDate = DateField()
    color = TextField()

    class Meta:
        database = db
        table_name = 'vehicles'


class Senders(Model):
    senderId = PrimaryKeyField()
    surname = TextField()
    name = TextField()
    patronymic = TextField()
    birthDate = DateField()
    postIndex = IntegerField()
    city = TextField()
    street = TextField()
    house = IntegerField()
    flat = IntegerField()
    phoneNumber = IntegerField()

    class Meta:
        database = db


class Recipients(Model):
    recipientId = PrimaryKeyField()
    surname = TextField()
    name = TextField()
    patronymic = TextField()
    birthDate = DateField()
    postIndex = IntegerField()
    city = TextField()
    street = TextField()
    house = IntegerField()
    flat = IntegerField()
    phoneNumber = IntegerField()

    class Meta:
        database = db


class Orders(Model):
    orderId = PrimaryKeyField()
    senderId = ForeignKeyField(Senders, backref="Orders")
    recipientId = ForeignKeyField(Recipients, backref="Orders")
    orderDate = DateField()
    deliveryDate = DateField()
    deliveryCost = IntegerField()
    courierId = ForeignKeyField(Couriers, backref="Orders")
    vehicleId = ForeignKeyField(Vehicles, backref="Orders")

    class Meta:
        database = db


db.connect()
db.create_tables([Senders, Recipients, Orders])
courier1, created = Couriers.get_or_create(
    surname="Herb",
    name="Bob",
    patronymic="Jr",
    passportNumber=999922,
    birthDate=date(2015, 2, 27),
    employmentDate=date(2023, 8, 11),
    workingDayStart=time(9, 16, 13),
    workingDayEnd=time(18, 37, 56),
    city="New York",
    street="Careless",
    house=13,
    flat=98,
    phoneNumber=2837192861
)

vehicle1 = Vehicles.get(Vehicles.vehicleId == 1)
sender1, created = Senders.get_or_create(surname="Sharapov",
                                         name="Rodion",
                                         patronymic="Alexeevich",
                                         birthDate=date(2005, 3, 17),
                                         postIndex=892819,
                                         city="New York",
                                         street="Big Main",
                                         house=52,
                                         flat=33,
                                         phoneNumber=9812749150)
sender2, created = Senders.get_or_create(surname="Karasev",
                                         name="Kirill",
                                         patronymic="Andreevich",
                                         birthDate=date(1978, 5, 26),
                                         postIndex=813245,
                                         city="New York",
                                         street="Saint Joe",
                                         house=25,
                                         flat=6,
                                         phoneNumber=23547484)
recipient1, created = Recipients.get_or_create(surname="Kostylev",
                                               name="Olexander",
                                               patronymic="Olegovich",
                                               birthDate=date(1978, 2, 12),
                                               postIndex="435227",
                                               city="Krakow",
                                               street="Kin",
                                               house=1,
                                               flat=12,
                                               phoneNumber=1231356)
recipient2, created = Recipients.get_or_create(surname="Matsumoto",
                                               name="Rangiku",
                                               patronymic="idk",
                                               birthDate=date(1231, 12, 1),
                                               postIndex="813245",
                                               city="Soul Society",
                                               street="Karakura",
                                               house=1,
                                               flat=1,
                                               phoneNumber=2315663)
order1, created = Orders.get_or_create(senderId=sender1,
                                       recipientId=recipient1,
                                       courierId=courier1,
                                       vehicleId=vehicle1,
                                       orderDate=date(2024, 12, 1),
                                       deliveryDate=date(2025, 1, 13),
                                       deliveryCost=1600,
                                       )
order2, created = Orders.get_or_create(senderId=sender2,
                                       recipientId=recipient2,
                                       courierId=courier1,
                                       vehicleId=vehicle1,
                                       orderDate=date(2024, 12, 1),
                                       deliveryDate=date(2025, 1, 13),
                                       deliveryCost=2600,
                                       )

db.close()
