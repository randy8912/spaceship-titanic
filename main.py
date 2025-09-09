import pandas as pd

# Load raw data
train = pd.read_csv('data/raw/train.csv')
test = pd.read_csv('data/raw/test.csv')

# Look into training data
print('Train shape:', train.shape)
print('Test shape:', test.shape)
print(train.head())