import pandas as pd
from openpyxl import Workbook, load_workbook

df = pd.read_excel('heart_2020_final2.xlsx')


print(df)
df.to_csv('heart_2020_final2.csv')