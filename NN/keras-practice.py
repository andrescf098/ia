import pandas as pd
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense

def run():
    filepath = './files/concrete_data.csv'
    df = pd.read_csv(filepath)
    columns = df.columns
    predictors = df[columns[columns != 'Strength']]
    target = df['Strength']
    predictors_norm = (predictors - predictors.mean()) / predictors.std()
    n_cols = predictors_norm.shape[1]
    model = regression_model(n_cols)
    model.fit(predictors_norm, target, validation_split=0.3, epochs=100, verbose=2)

def regression_model(n_cols):
    model = Sequential()
    model.add(Dense(50, activation='relu', input_shape=(n_cols,)))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    return model


if __name__ == '__main__':
    run()