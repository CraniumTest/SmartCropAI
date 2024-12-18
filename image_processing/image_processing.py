import cv2
import numpy as np
import tensorflow as tf

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (256, 256))
    image = np.array(image) / 255.0
    return image

def load_model(model_path):
    return tf.keras.models.load_model(model_path)

def predict(image, model):
    prediction = model.predict(image[np.newaxis, ...])
    return prediction
