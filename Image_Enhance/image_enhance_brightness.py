from PIL import Image, ImageEnhance
# Opening Image
im =Image.open("../img/leo.jpg")
# Creating object of Color class
im3 = ImageEnhance.Brightness(im)

# showing resultant image
im3.enhance(1.0).show() # original image
im3.enhance(3.0).show()
im3.enhance(10.0).show() # white image