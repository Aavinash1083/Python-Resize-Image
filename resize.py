from PIL import Image
foo = Image.open("/home/aavinash1083/Python/Vijay.jpeg")
foo.size
(200,374)
foo = foo.resize((160,300),Image.ANTIALIAS)
foo.save("/home/aavinash1083/Python/Vijay1.jpeg",quality=95)
foo.save("/home/aavinash1083/Python/Vijay2.jpeg",optimize=True,quality=95)

