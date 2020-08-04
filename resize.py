from PIL import Image
img = Image.open("/home/aavinash1083/CELERY/IMAGES.jpeg")
img.size
(200,374)
img = img.resize((160,300),Image.ANTIALIAS)
img.save("/home/aavinash1083/CELERY/IMAGES1.jpeg",quality=85)
img.save("/home/aavinash1083/CELERY/IMAGES2.jpeg",optimize=True,quality=75)

