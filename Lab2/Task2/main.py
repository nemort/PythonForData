from PIL import Image
from sys import argv


with Image.open(argv[1]) as img:
    img.load()

red = green = blue = 0
for i in img.getdata():
    red += i[0]
    green += i[1]
    blue += i[2]

if red > green and red > blue:
    print('Больше всего используется красный')
elif green > red and green > blue:
    print('Больше всего используется зеленый')
else:
    print('Больше всего используется синий')
