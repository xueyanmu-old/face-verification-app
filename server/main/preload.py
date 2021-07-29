import tensorflow as tf
from PIL import Image
from io import BytesIO
from deepface import DeepFace

with open("main/test_image.png", "rb") as image:
    f = image.read()
    b = bytearray(f)
    img = Image.open(BytesIO(b))
image_array = tf.keras.preprocessing.image.img_to_array(img)

# demography = DeepFace.analyze(image_array, actions=["emotion"])
demography = DeepFace.analyze(image_array, enforce_detection=False, actions=["age"])


result = DeepFace.verify(image_array, image_array, enforce_detection=False, model_name="Facenet")
print("Is verified: ", result["verified"])
