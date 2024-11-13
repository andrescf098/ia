import keras
from keras.utils import to_categorical
from keras.datasets import mnist
from NN_models.convolutional_two import convolutional_model

def run():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Reshape to be [samples][pixels][width][height]
    X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32')

    # Normalize inputs from 0-255 to 0-1
    X_train = X_train / 255
    X_test = X_test / 255

    # One hot encode outputs
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    num_classes = y_test.shape[1]

    # Train the model
    model = convolutional_model(num_classes)
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=200, verbose=2)

    # Final evaluation of the model
    scores = model.evaluate(X_test, y_test, verbose=0)
    model.save('./files/models/convolutional_model_2.h5')
    return print('Accuracy: {}% \n Error: {}'.format(scores[1], 1 - scores[1]))

if __name__ == '__main__':
    run()