from PIL import Image, ImageDraw, ImageFont


def draw(number):
    img = Image.new('RGB', (100, 100))

    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 99, 99), outline='blue', width=5)

    draw.text((img.size[0] // 2, img.size[1] // 2),
              str(number),
              fill='red',
              font=ImageFont.truetype('arial.ttf', 52),
              anchor='mm')

    img.show()
    img.save(f'img{number}.png', 'png')


for i in range(1, 4):
    draw(i)
