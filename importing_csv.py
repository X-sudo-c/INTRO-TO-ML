import pandas as pd

data_path = "/home/x-x/Documents/INTRO-TO-ML/melb_data.csv"

data = pd.read_csv(data_path)

print(data.describe())

print(data.columns)

# print(data.dropna(axis=0))

# print(data.price)