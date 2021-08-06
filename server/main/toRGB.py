from PIL import Image
from deepface import DeepFace
import tensorflow as tf

image1 = Image.open('ay1.png')
img1 = image1.convert('RGB')
rgb1 = img1.save("ayrbg1.jpg")
img1 = tf.keras.preprocessing.image.img_to_array(img1)

image2 = Image.open('ay2.png')
img2 = image2.convert('RGB')
rgb2 = img2.save("ayrbg2.jpg")
img2 = tf.keras.preprocessing.image.img_to_array(img2)
#
# # save to database
# instance = compare()
# instance.first.put(io.BytesIO(file[0]))
# instance.second.put(io.BytesIO(file[1]))
# instance.save()

# try:
result = DeepFace.verify(img1, img2, model_name="Facenet", enforce_detection=False)
# except:
#     result = "L"
print({"result": result})
