import pickle
import tensorflow as tf
import numpy as np
import cv2
import base64
import io
from skimage.transform import resize


foods = ['apple', 'asparagus', 'banana', 'broccoli', 'onion', 'pineapple', 'strawberry', 'watermelon']


def decodeMetadata(s):
    return base64.b64decode(s[21:])

def load_files(path, _svd, _scaler):
    model = tf.keras.models.load_model(path + 'neuralNet')

    with open(_svd, "rb") as f:
        svd = pickle.load(f)
    
    with open(_scaler, "rb") as f:
        scaler = pickle.load(f)
    
    return model, svd, scaler

def labeled(preds):
    for p in preds:
        dic = {}
        for i in range(8):
            dic[foods[i]] = p[i]
    return dic

def nLargest(n, dic):
    base = [("",0) for i in range(n)]
    for k in dic.keys():
        if dic[k] > base[0][1]:
            base[0], base[1], base[2] = (k, dic[k]) , base[0], base[1]
        elif dic[k] > base[1][1]:
            base[1], base[2] = (k, dic[k]), base[1]
        elif dic[k] > base[2][1]:
            base[2] = (k, dic[k])
    return base


def predictImg(data):
    
    # Carga de modelos

    model, svd, scaler  = load_files("./mlmodel/model/models/", "./mlmodel/model/models/compresser", "./mlmodel/model/models/scaler")

    # Obtencion de la imagen a partir de la metadata

    png = np.asarray(bytearray(decodeMetadata(data)), dtype="uint8")

    image = cv2.imdecode(png, cv2.IMREAD_GRAYSCALE)


    # Resize y conversion de la matriz al estilo del dataset
    
    image = resize(image, (32,32))
    
    image = (1-image) * 255

    #conversion 0-1 

    ruido = 20 # variable para reducir el ruido de la imagen

    image = np.array([1 if p>ruido else 0 for p in image.reshape(-1)]).reshape(1,1024)
    
    pickle.dump(image, open("img.pkl", 'wb'))

    # Reduccion de dimensiones

    red = svd.transform(image)

    # Escalar la reduccion con el scaler

    red = scaler.transform(red)

    print(red)

    # predicciones 

    preds = model.predict(red)
    
    print(labeled(preds))

    return nLargest(3, labeled(preds))