import os
from PIL import Image
for filename in os.listdir('banners'):
    image = Image.open('banners/'+filename)
    newimage = image.resize((1920,640))
    newimage.save('resizedbanners/resize'+filename)
