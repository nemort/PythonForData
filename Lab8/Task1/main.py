import sqlite3

conn = sqlite3.connect('orders.db')
cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS orders(
#     orderId INTEGER PRIMARY KEY AUTOINCREMENT,
#     senderId INTEGER,
#     recipient INTEGER,
#     orderDate DATE,
#     deliveryDate DATE,
#     deliveryCost INTEGER,
#     courierId INTEGER,
#     vehicleId INTEGER);
# """)
#
# cur.execute("""CREATE TABLE IF NOT EXISTS sender(
#     senderId INTEGER PRIMARY KEY AUTOINCREMENT,
#     surname TEXT,
#     name TEXT,
#     patronymic TEXT,
#     birthDate DATE,
#     postIndex INTEGER,
#     city TEXT,
#     street TEXT
#     house INTEGER,
#     flat INTEGER,
#     phoneNumber INTEGER);
# """)
#
# cur.execute("""CREATE TABLE IF NOT EXISTS recipient(
#     recipientId INTEGER PRIMARY KEY AUTOINCREMENT,
#     surname TEXT,
#     name TEXT,
#     patronymic TEXT,
#     birthDate DATE,
#     postIndex INTEGER,
#     city TEXT,
#     street TEXT
#     house INTEGER,
#     flat INTEGER,
#     phoneNumber INTEGER);
# """)

cur.execute("""CREATE TABLE IF NOT EXISTS vehicles(
    vehicleId INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT,
    registrationDate DATE,
    color TEXT);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS couriers(
    courierId INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT,
    name TEXT,
    patronymic TEXT,
    passportNumber INTEGER,
    birthDate DATE,
    employmentDate DATE,
    workingDayStart TIME,
    workingDayEnd TIME,
    city TEXT,
    street TEXT,
    house INTEGER,
    flat INTEGER,
    phoneNumber INTEGER);
""")

cur.execute("""INSERT INTO vehicles(brand, registrationDate, color)
    VALUES('Lotus', '2021-07-17', 'yellow')""")

cur.execute("""UPDATE vehicles
    SET color = 'red'
    WHERE vehicleId = 1
""")

cur.execute("""INSERT INTO vehicles(brand, registrationDate, color)
    VALUES('BMW', '2013-12-27', 'black')""")

conn.commit()
