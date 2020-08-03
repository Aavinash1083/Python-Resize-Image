from PIL import Image
img = Image.open("/home/aavinash1083/CELERY/Vijay.jpeg")
img.size
(200,374)
img = img.resize((160,300),Image.ANTIALIAS)
img.save("/home/aavinash1083/CELERY/Vijay1.jpeg",quality=95)
img.save("/home/aavinash1083/CELERY/Vijay2.jpeg",optimize=True,quality=95)

