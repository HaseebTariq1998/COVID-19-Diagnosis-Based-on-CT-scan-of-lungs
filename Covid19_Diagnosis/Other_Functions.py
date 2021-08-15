import pymongo
import time
import cv2
import numpy as np
import datetime


#calculate past 6 dates from current current date
def dates_generator():
    dates_lists = []
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    now = datetime.datetime.now()
    M = now.strftime("%m")
    Y = now.strftime("%Y")
    D = now.strftime("%d")
    now_d = now.strftime("%Y-%m-%d")
    dates_lists.append(now_d)
    D = int(D)
    Y = int(Y)
    M = int(M)
    l = []
    for n in range(0, 6):
        if ((D - 1) == 0):
            if (M - 1 == 0):
                Y = Y - 1
                M = 12
                D = 31
            else:
                M = M - 1
                D = months_days[M - 1]
        else:
            D = D - 1
        x = datetime.datetime(Y, M, D)
        x = x.strftime("%Y-%m-%d")
        dates_lists.append(x)
    return dates_lists

# apply preprocessing
def prepare(x):
    IMG_SIZE = 224 # 50 in txt-based
    new_array = cv2.resize(x, (IMG_SIZE, IMG_SIZE))
    new_array=new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)
    new_array=new_array/255.0
    return new_array

# classifier
def test(img):
    from tensorflow.keras import models
    img = prepare(img)
    model1 = models.load_model('x3.h5')
    r = model1.predict([img])
    if r[0][0] > r[0][1] and r[0][0] > r[0][2]:
        return"CONTROL"
    elif r[0][1] > r[0][0] and r[0][1] > r[0][2]:
        return "REGULAR"
    else:
        return "SEVERE"