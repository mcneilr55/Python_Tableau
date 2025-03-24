# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:05:09 2024

@author: rmcneil
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe data for specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualinc'] = income

#working with arrays

#1D array
arr = np.array([1,2,3,4])

#0D array
arr = np.array([43])

#2D array
arr = np.array([[1,2,3], [4,5,6]])

#working with IF Statements
a = 40
b = 500
c = 20
if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('no conditions met')


#If statement based on FICO score
fico = 250

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)


#For Loop
fruits = ['apple', 'pear', 'banana', 'cherry']

for x in fruits:
    print(x)
    y = x+ ' fruit'
    print(y)
    
for x in range(0,3):
    y = fruits[x]
    print(y)    
    
    
#For loops to loan data  
length = len(loandata)  
#variable blank column
ficocat = []
for x in range(0, length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'   
    except:         
        cat = 'Unknown'
        
    #appends to new column
    ficocat.append(cat)
#convert list to series (column in the data frame)
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

# #While loops
# i = 1
# while i < 10:
#     print (i)
#     i = i + 1
    
    
# #testing Error
# #For loops to loan data  
# length = len(loandata)  
# #variable blank column
# ficocat = []
# for x in range(0, length):
#     category = 'red'
    
#     try:
#         if category >= 300 and category < 400:
#             cat = 'Very Poor'
#         elif category >= 400 and category < 600:
#             cat = 'Poor'
#         elif category >= 601 and category < 660:
#             cat = 'Fair'
#         elif category >= 660 and category < 780:
#             cat = 'Good'
#         elif category >= 780:
#             cat = 'Excellent'
#         else:
#             cat = 'Unknown'   
#     except:
#             cat = 'ERROR'
#     #appends to new column
#     ficocat.append(cat)
    
    
# #convert list to series (column in the data frame)
# ficocat = pd.Series(ficocat)
# loandata['fico.category'] = ficocat
    

#df.loc as conditional statements
# df.loc[df[columnname] condition, newcolumnname] = 'value if condition is met'

#for insterest rates, a new column is wanted. rate > 0.12 then high, else low
loandata.loc[loandata['int.rate'] > .12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= .12, 'int.rate.type'] = 'Low'


#number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = .75)
plt.show()

purposeplot = loandata.groupby(['purpose']).size()
purposeplot.plot.bar(color = 'orange', width = .75)
plt.show()

#scatter plot; need a x & y
#if high annual income is debt to income low?
ypoint = loandata['annualinc']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint)
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv', index=True)
