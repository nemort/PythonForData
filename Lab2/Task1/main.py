from PIL import Image


with Image.open('img.png') as img:
    img.load()

red, green, blue, alpha = img.split()

zeroed_band = red.point(lambda _: 0)

img.show()
Image.merge('RGB', (red, zeroed_band, zeroed_band)).show()
Image.merge('RGB', (zeroed_band, green, zeroed_band)).show()
Image.merge('RGB', (zeroed_band, zeroed_band, blue)).show()
