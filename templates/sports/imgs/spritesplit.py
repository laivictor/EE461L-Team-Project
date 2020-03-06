from PIL import Image
from os import mkdir

sheet = Image.open("sportssprite.png")

for x in range(70):
    a = (x + 1) * 96
    icon = sheet.crop((0, a-96, 96, a)
    icon.save("{}.png".format(x))
