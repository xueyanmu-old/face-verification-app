import tensorflow as tf
from tensorflow import keras
from PIL import Image
from io import BytesIO
from deepface import DeepFace

with open("/heroku/main/image.jpeg", "rb") as image:
    f = image.read()
    b = bytearray(f)
    img = Image.open(BytesIO(b))
image_array = tf.keras.preprocessing.image.img_to_array(img)

demography = DeepFace.analyze(image_array, actions=["emotion"], enforce_detection=False)

result = DeepFace.verify(image_array, image_array, model_name="Facenet", enforce_detection=False)
print("Is verified: ", result["verified"])
