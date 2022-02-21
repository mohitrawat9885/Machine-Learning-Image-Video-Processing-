from PIL import Image, ImageEnhance
im = Image.open("../img/3.jpg")
im3 = ImageEnhance.Contrast(im)

im3.enhance(1.0).show() # Original

im3.enhance(10.0).show() # Dark Image