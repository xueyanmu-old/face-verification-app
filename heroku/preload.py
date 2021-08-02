import tensorflow as tf
from tensorflow.keras import preprocessing
from PIL import Image
from io import BytesIO
from deepface import DeepFace

with open("/heroku/image.jpeg", "rb") as image:
    f = image.read()
    b = bytearray(f)
    img = Image.open(BytesIO(b))
image_array = tf.keras.preprocessing.image.img_to_array(img)

demography = DeepFace.analyze(image_array, actions=["emotion"])

result = DeepFace.verify(image_array, image_array, model_name="Facenet", enforce_detection=False)
print("Is verified: ", result["verified"])
