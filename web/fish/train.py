import numpy
from tensorflow.python.keras.datasets import mnist
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.callbacks import TensorBoard
from tensorflow.python.keras.utils import to_categorical

def load_data():
    #とりあえず仮でMNISTのデータ返却
    (x_train,y_train), (x_test,y_test) = mnist.load_data()
    return (x_train,y_train), (x_test,y_test)

def execute_train(train, test):
    x_train = train[0]
    y_train = train[1]

    x_train = x_train.reshape(60000,784)
    x_train = x_train/255

    y_train = to_categorical(y_train,10)

    model = Sequential()
    model.add(
            Dense(
                units = 64,
                input_shape=(784,),
                activation='relu'
            )
    )
    model.add(
            Dense(
                units = 10,
                activation='softmax'
            )
    )
    model.compile(
        optimizer='adam',
        loss = 'categorical_crossentropy',
        metrics=['accuracy']
    )
    tsb=TensorBoard(log_dir='./logs')
    history_adam=model.fit(
        x_train,
        y_train,
        batch_size=32,
        epochs=20,
        validation_split=0.2,
        callbacks=[tsb]
    )
    
if __name__ == '__main__':
    train, test = load_data()
    execute_train(train,test)