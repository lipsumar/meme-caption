from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("images/one-does-not-simply.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("impact.ttf", 52)

draw.text((10, 10), "Hello world", (255,255,255), font=font)
img.save("out.jpg")
