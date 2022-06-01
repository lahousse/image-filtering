################# Henri Lahousse #################
# paste image on top of other image

from PIL import Image

img = Image.open(r"ENTER_PATH") 
#print(img.size)

background = Image.open(r"ENTER_PATH") 
#print(background.size)


# resize the image
size = (277,182)
background = background.resize(size,Image.ANTIALIAS)
img = img.resize(size,Image.ANTIALIAS)

background.paste(img, (0, 0)) # paste images on top of each other
background.save(r"ENTER_PATH") # save image