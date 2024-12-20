import pandas as pd
import numpy as np

#-----------------------------------Basic QUestions Common For All--------------------------

df=pd.read_csv(r"C:\Users\techs\OneDrive\Desktop\Class python\Labexam\AQI_Data.csv")

#Display First 8 rows


print('                                --------------These Are First 8 Rows-----------------')
print(df.head(8))



#Display last 5 rows
print('                                --------------These Are Last 5 Rows-----------------')

print(df.tail(5))



#show dtype and number of not null values in each column
print('                       --------------These Are Data Type Of Each Column In The DataFrame-----------------')

print(df.dtypes)

print(                '--------------These Are Total Non Null values In each  Column Of The DataFrame-----------------')

print(df.notnull().sum())

#Dispaly mean max and min for required columns city wise for each city

print('      --------------These Are Mean , Max , Min of AQI , PM2.5 ,PM10 column Respectively  City Wise-----------------')

result = df.groupby('City').agg(
    mean_AQI=('AQI', 'mean'),
    max_PM2=('PM2.5', 'max'),
    min_PM10=('PM10', 'min')
    
).reset_index()

print(result)


#--------------------------------------------SET 2 Solutions-----------------------------------------------!

#Renaming of Given Columns


df.rename(columns={'AQI':'Air Quality index','PM2.5':'Particulate Matter 2.5','PM10':'Particulate Matter 10','City':'Location'}, inplace=True)

print("                     --------------------------Renamed Columns--------------------------------")

print(df.head(2))

#Repalcing 'unknown' value Of city Column to A 'NotAvailable'

df1=df.replace('Unknown','Not Available')


#Saving file "result.csv"

df1.to_csv('result.csv',index=False)
