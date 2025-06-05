import pandas as pd

data_path = "/home/x-x/Documents/INTRO-TO-ML/melb_data.csv"

data = pd.read_csv(data_path)

print(data.describe())

print(data.columns)

print(data.dropna(axis=0))

print(data.price) #collums are stored as methods so to list a colum you can just call it with the method

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude' ]

X = data[melbourne_features]

X.describe()

X.head()

#consistency is the key
#let me commit additional code
