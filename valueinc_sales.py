# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:16:27 2024

@author: rmcneil
"""

import pandas as pd

# file_name = pd.read_csv ('file.csv')  <---format of read_csv
# file_name = pd.read_csv('transaction2.csv') 

data = pd.read_csv('transaction2.csv', sep=';') 

#summary of the data
data.info()

# defining variables
CostperItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

ProfitperItem = SellingPricePerItem - CostperItem
ProfitperTransaction = ProfitperItem * NumberofItemsPurchased
CostperTransaction = CostperItem * NumberofItemsPurchased
SellingperTransaction = SellingPricePerItem * NumberofItemsPurchased

# cost per transaction col calculation

#CostperTransaction = CostperItem * NumberofItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostperTransaction = CostPerItem * NumberofItemsPurchased

# adding new column

data['CostperTransaction'] = CostperTransaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

data['ProfitperTransaction'] = (data['SalesPerTransaction'] - data['CostperTransaction'])

data['Markup'] = data['ProfitperTransaction'] / data['CostperTransaction']

#Rounding Marking

RoundMarkup = round(data['Markup'], 2)
data['Markup'] = RoundMarkup

#combining data fields
my_name = 'Deez'+'Nutz'
my_date='Day'+'-'+'Month'+'-'+'Year'

day = data['Day'].astype(str)
year = data['Year'].astype(str)

my_date = day+'-'+data['Month']+'-'+year

data['date'] = my_date

#split field and assign to new columns
sp_col=data['ClientKeywords'].str.split(',', expand=True)
data['ClientAge']=sp_col[0]
data['ClientType']=sp_col[1]
data['ClientLength']=sp_col[2]

#replace
data['ClientAge']=data['ClientAge'].str.replace('[','')
data['ClientLength']=data['ClientLength'].str.replace(']','')

#lower-case
data['ItemDescription']=data['ItemDescription'].str.lower()

#merge files
#bring new data set
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')
#merging files
data = pd.merge(data,seasons, on='Month')

#dropping columns
data = data.drop('ClientKeywords', axis=1)
data = data.drop('Day', axis=1)
data=data.drop(['Year', 'Month'], axis=1)

#export into csv
data.to_csv('ValueInc_Cleaned.csv', index=False)


