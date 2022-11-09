import pickle
from PIL import Image
import numpy as np
import cv2


foods = ["apple","asparagus","banana","blackberry","broccoli","grapes","onion","pineapple","strawberry","watermelon"]


import base64
import io

def decodeMetadata(s):
    png_recovered = base64.b64decode(s[21:])
    return io.BytesIO(png_recovered)

def encodeMetadata(s):
    return '%s,%s' % ('data:image/png;base64',base64.b64encode(s.getvalue()).decode())


def load_files(_knn, _svd):
    with open(_knn, "rb") as f:
        knn = pickle.load(f)

    with open(_svd, "rb") as f:
        svd = pickle.load(f)
    return knn, svd


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


def predictImg(data, decoded=False):
    '''
    Se usan modelos Desarrolados en los siguiente notebooks:
    KNN:
    SVD:
    '''
    knn, svd = load_files("./mlmodel/model/models/pca50/model", "./mlmodel/model/models/pca50/compresser")
    metadata = ""

    if not decoded:
        png = decodeMetadata(data)
    else:
        png = data
        metadata = encodeMetadata(data)

    img = Image.open(png).convert("L")
    matriz = np.matrix(img)
    r = cv2.resize(255-matriz, dsize=(128, 128)).reshape(-1)
    dat = svd.transform(r.reshape(1,-1))
    preds = knn.predict_proba(dat)
    dic = {foods[i]: float(preds[0][i]) for i in range(len(foods))}
    return nLargest(3, dic), metadata
