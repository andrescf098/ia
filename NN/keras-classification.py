import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras.datasets import mnist
import matplotlib.pyplot as plt

def run():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    # print(X_train.shape)
    # print(plt.imshow(X_train[0]))

    # Flatten the images to one dimension
    num_pixels = X_train.shape[1] * X_train.shape[2]
    X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32')
    # Normalize the pixel values to be between 0 and 1
    X_train = X_train / 255
    X_test = X_test / 255
    # One hot encode outputs
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    num_classes = y_test.shape[1]
    # Train the model
    model = classification_model(num_pixels, num_classes)
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, verbose=2)
    # Final evaluation of the model
    scores = model.evaluate(X_test, y_test, verbose=0)
    # Save the model
    model.save('./files/models/classification_model.h5')
    return print('Accuracy: {}% \n Error: {}'.format(scores[1], 1 - scores[1]))

def classification_model(num_pixels, num_classes):
    model = Sequential()
    model.add(Dense(num_pixels, activation='relu', input_shape=(num_pixels,)))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

if __name__ == '__main__':
    run()