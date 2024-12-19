from PIL import Image, ImageFilter


with Image.open('watermark.png') as watermark, Image.open('img.png') as img:
    watermark.load()
    img.load()

watermark = (watermark.convert("L").
             point(lambda x: 255 if x > 50 else 0).
             filter(ImageFilter.CONTOUR).
             point(lambda x: 255 if x == 0 else 0).
             crop((1, 1, watermark.width - 1, watermark.height - 1)))

img.paste(watermark, (img.width // 2 - watermark.width // 2, img.height // 2 - watermark.height // 2), watermark)
img.show()
img.save('img_with_watermark.JPG', 'JPEG')
