from tensorflow.keras.applications import MobileNet
from tensorflow.keras.applications.mobilenet import preprocess_input, decode_predictions
import numpy as np
import tensorflow as tf

model = MobileNet()
img = tf.keras.utils.get_file(
    "elephant.jpg", "https://storage.googleapis.com/download.tensorflow.org/example_images/320px-Elephant_During_Sunset.jpg")
img = tf.keras.preprocessing.image.load_img(img, target_size=(224, 224))
x = tf.keras.preprocessing.image.img_to_array(img)
x = preprocess_input(np.expand_dims(x, axis=0))
preds = model.predict(x)
print(decode_predictions(preds, top=1)[0])
