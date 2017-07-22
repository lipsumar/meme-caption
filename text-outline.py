from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("image.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("impact.ttf", 52)

textX = 10
textY = 10
text = "Hello outline"

draw.text((textX-2, textY-2), text,(0,0,0),font=font)
draw.text((textX+2, textY-2), text,(0,0,0),font=font)
draw.text((textX+2, textY+2), text,(0,0,0),font=font)
draw.text((textX-2, textY+2), text,(0,0,0),font=font)
draw.text((textX, textY), text, (255,255,255), font=font)
img.save("out.jpg")
