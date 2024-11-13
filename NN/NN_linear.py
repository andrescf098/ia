import pandas as pd
import keras

filepath = './files/concrete_data.csv'
df=pd.read_csv(filepath)

df.dropna(inplace=True)