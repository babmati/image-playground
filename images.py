from PIL import Image, ImageFilter
# we had to install Pillow Libray

#1234567
img =  Image.open('.\Pokedex\pikachu.jpg')

# print(img.size) # .format , .size , .mode ,
#
# print(dir(img))  ## this tell properties and attributes image has
#
# filtered_img= img.filter(ImageFilter.SMOOTH)  # WE CAN CHECK MORE FILTERS TO USE(SMOOTTH, SHARPEN, BLUR)
# filtered_img = img.convert('L')
# filtered_img.save("Grey.png",'png')
# filtered_img.show()   # this let me see the image
# crooked = filtered_img.rotate(90)  # this will let me rotate the image
# crooked.save("rotate.png", 'png')
# resize = filtered_img.resize((300, 300))   # this allows me to resize
# resize.save("imgsized.png", "png")

# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("crop.png", "png")

# imgcab = Image.open('.\Pokedex\imgcab.jpg')
# print(imgcab.size)
#
#
# # new_img=imgcab.resize((400,400)) this will make the image more clear
# # new_img.save("tumbnail.jpg") #
#
# imgcab.thumbnail((400,400))
# imgcab.save("tumbnail1.jpg")




