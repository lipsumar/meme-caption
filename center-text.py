from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("image.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("impact.ttf", 42)

def drawTextWithOutline(text, x, y):
    draw.text((x-2, y-2), text,(0,0,0),font=font)
    draw.text((x+2, y-2), text,(0,0,0),font=font)
    draw.text((x+2, y+2), text,(0,0,0),font=font)
    draw.text((x-2, y+2), text,(0,0,0),font=font)
    draw.text((x, y), text, (255,255,255), font=font)
    return

text = "Are we centered yet?"
w, h = draw.textsize(text, font) # measure the size the text will take
drawTextWithOutline(text, img.width/2 - w/2, 10)

img.save("out.jpg")
