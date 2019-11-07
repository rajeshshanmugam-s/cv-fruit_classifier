import json
import numpy as np
import tensorflow as tf
import cv2
from keras.models import load_model


model = load_model('fruit_classifier.h5')
json_file = open('labels.json')
json_file_str = json_file.read()
label_to_id_dict = json.loads(json_file_str)


def predictor(image_url=None, image_path=None, cnn=True):
    if image_url:
        image_extension = image_url[-4:]
        image_path = tf.keras.utils.get_file('image'+image_extension,
                                             origin=image_url)
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (45, 45))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    image_list = []
    image_list.append(image)

    image_arr = np.array(image_list)

    image = image_arr/255
#     input_shape=(45, 45, 3)

#     if model != 'model_cnn':
#         print('passed')
    if not cnn:
        image = image.reshape(image.shape[0], 45*45*3)

    class_predicted = model.predict_classes(image)

    in_id = class_predicted[0]

    inv_map = {v: k for k, v in label_to_id_dict.items()}

    return inv_map[in_id]