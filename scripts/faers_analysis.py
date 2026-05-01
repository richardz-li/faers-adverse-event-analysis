import pandas as pd

drug_df = pd.read_csv('C:/Users/richa/Desktop/Projects/Data/DEMO25Q4.txt', delimiter = '$', encoding = 'latin-1')
reac_df = pd.read_csv('C:/Users/richa/Desktop/Projects/data/REAC25Q4.txt', delimiter = '$', encoding = 'latin-1')
demo_df = pd.read_csv('C:/Users/richa/Desktop/Projects/data/DEMO25Q4.txt', delimiter = '$', encoding = 'latin-1')
outc_df = pd.read_csv('C:/Users/richa/Desktop/Projects/data/OUTC25Q4.txt', delimiter = '$', encoding = 'latin-1')

print(drug_df.head())

print(drug_df.shape)

print(drug_df.columns.tolist())

print(drug_df.isnull().sum())

print(drug_df.describe())