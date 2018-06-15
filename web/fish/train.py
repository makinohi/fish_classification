import os
import keras
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.preprocessing.image import array_to_img, img_to_array, list_pictures, load_img
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

epochs = 20
batch_size = 32
img_size = (128,128)
category_size = 3
model_file_path = './model/model_weight.h5'

def load_data():
    x_data = []
    y_data = []

    # appleの画像
    for picture in list_pictures('./dataset/apple/'):
        img = img_to_array(load_img(picture, target_size=img_size))
        x_data.append(img)
        y_data.append(0)

    # bananaの画像
    for picture in list_pictures('./dataset/banana/'):
        img = img_to_array(load_img(picture, target_size=img_size))
        x_data.append(img)
        y_data.append(1)

    # orangeの画像
    for picture in list_pictures('./dataset/orange/'):
        img = img_to_array(load_img(picture, target_size=img_size))
        x_data.append(img)
        y_data.append(2)

    # arrayに変換
    x_data = np.asarray(x_data)
    y_data = np.asarray(y_data)

    # 画素値を0から1の範囲に変換
    x_data = x_data.astype('float32')
    x_data = x_data / 255.0

    # クラスの形式を変換
    y_data = np_utils.to_categorical(y_data, category_size)

    # 学習用データとテストデータの振り分け
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.33, random_state=123)

    return x_train, x_test, y_train, y_test

def create_model():
    model = Sequential()

    model.add(Conv2D(32, (3, 3), padding='same',
                    input_shape = (128,128,3)))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(category_size))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
                optimizer='rmsprop',
                metrics=['accuracy']) 
    return model

def load_weight(model, file_path):
    if not os.path.exists(file_path):
        return 
    model.load_weights(file_path)

def fit(model, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_data = (x_test, y_test))
    model.save(model_file_path)

if __name__ == '__main__':

    #教師用データ、テスト用データ読込
    x_train, x_test, y_train, y_test = load_data()

    #モデル生成
    model = create_model()

    #重み読込
    load_weight(model,model_file_path)

    #学習
    fit(model, x_train, x_test, y_train, y_test)