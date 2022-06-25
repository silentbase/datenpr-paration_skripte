import pandas as pd
from openpyxl import Workbook, load_workbook

df = pd.read_excel('heart_2020.xlsx')
print(df)
for i in range(0, len(df.columns)):
    for j in range (0, len(df.index)):
        if df.iat[j,i] == 'No' or df.iat[j,i] == 'Female': # No = Female = 0

            df.iat[j,i] = 0
        elif str(df.iat[j,i]).find('No') != -1: # No, borderline diabetes = 2
                df.iat[j,i] = 2
        elif df.iat[j,i] == 'Yes' or df.iat[j,i] == 'Male': # Yes = Male = 1
            df.iat[j,i] = 1       
        elif str(df.iat[j,i]).find('Yes') != -1:    # Yes, during pregnancy = 3
            df.iat[j,i] = 3
        elif df.iat[j,i] == 'White': # White = 0
            df.iat[j,i] = 0
        elif df.iat[j,i] == 'Black': # Black = 1
            df.iat[j,i] = 1
        elif df.iat[j,i] == 'Hispanic': # Hispanic = 2
            df.iat[j,i] = 2
        elif df.iat[j,i] == 'Asian': # Asian = 3
            df.iat[j,i] = 3
        elif df.iat[j,i] == 'American Indian/Alaskan Native': # American Indian/Alaskan Native = 4
            df.iat[j,i] = 4                
        elif df.iat[j,i] == 'Other': # Other = 5
            df.iat[j,i] = 5

print(df)
df.to_excel('heart_2020_edited.xlsx')
