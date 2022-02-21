from PIL import Image, ImageFilter

image = Image.open("../img/obj.jpg")
image.show()
image = image.convert("L")
image.show()
image = image.filter(ImageFilter.FIND_EDGES)
image.save('segmented image.jpg')
image.show()