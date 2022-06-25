import pandas as pd
from openpyxl import Workbook, load_workbook

df = pd.read_excel('heart_2020_edited.xlsx')

for i in range(0, len(df.index)): #categorize BMI & code
    if float(df.iat[i,2]) < 18.5:
        df.iat[i,2] = '0'
    elif float(df.iat[i,2]) > 18.5 and float(df.iat[i,2]) < 24.99:
        df.iat[i,2] = '1'    
    elif float(df.iat[i,2]) >= 25 and float(df.iat[i,2]) <= 29.99:
        df.iat[i,2] = '2'
    elif float(df.iat[i,2]) >= 30:
        df.iat[i,2] = '3'    

for i in range(0, len(df.index)): #health code
    if df.iat[i,17] == 'Poor':
        df.iat[i,17] = '0'
    elif df.iat[i,17] == 'Fair':     
        df.iat[i,17] = '1'
    elif df.iat[i,17] == 'Good':     
        df.iat[i,17] = '2'
    elif df.iat[i,17] == 'Very good':     
        df.iat[i,17] = '3'
    elif df.iat[i,17] == 'Excellent':     
        df.iat[i,17] = '4'             

for i in range(0, len(df.index)): #Age code
    if df.iat[i,10] == '18-24':
        df.iat[i,10] = '0'
    elif df.iat[i,10] == '25-29':     
        df.iat[i,10] = '1'
    elif df.iat[i,10] == '30-34':     
        df.iat[i,10] = '2'
    elif df.iat[i,10] == '35-39':     
        df.iat[i,10] = '3'
    elif df.iat[i,10] == '40-44':     
        df.iat[i,10] = '4'
    elif df.iat[i,10] == '45-49':     
        df.iat[i,10] = '5'
    elif df.iat[i,10] == '50-54':     
        df.iat[i,10] = '6'
    elif df.iat[i,10] == '55-59':     
        df.iat[i,10] = '7'                
    elif df.iat[i,10] == '60-64':     
        df.iat[i,10] = '8'
    elif df.iat[i,10] == '65-69':     
        df.iat[i,10] = '9'
    elif df.iat[i,10] == '70-74':     
        df.iat[i,10] = '10'
    elif df.iat[i,10] == '75-79':     
        df.iat[i,10] = '11'  
    elif df.iat[i,10] == '80 or older':     
        df.iat[i,10] = '12'
      
df.to_excel('heart_2020_final2.xlsx')        