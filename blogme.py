# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:53:09 2025

@author: rmcneil
"""
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = pd.read_excel('articles.xlsx')
#summary of the data
data.describe()

#summary of the columns
data.info()

#Group by function; # of articles per source
data.groupby(['source_id'])['article_id'].count()
#number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping column
data=data.drop('engagement_comment_plugin_count' , axis=1)

#functions
def thisFunction():
    print('My first function, BIATCH!')

thisFunction()

#function w/ variables
def aboutMe(name, surname, location):
    print('This is ' + name+'. My pronouns are '+surname+'. I am a lesbian in the '+location)
    return name, surname, location

a = aboutMe('Jordan','Them/They','Bahamas')

#function w/ For Loops
def favFood(food):
    for x in food:
        print('Top food is '+x)

fastFood = ['burgers', 'pizza', 'pie']

favFood(fastFood)

#----------------------------------
#keyword flag w/ in title
keyword = 'crash'

#for loop
#find the total number of rows
# length = len(data)
# #creating a new column
# keyword_flag = []
# for x in range(0,length):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)


#creating a function, user inputs keyword
def keywordFlag(keyword):
    length=len(data)
    #creating a new column
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        # if encounter error (e.g., Null value) assign a 0 value    
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
    
k = keywordFlag('murder')

#create new col in dataframe
data['keyword_flag'] = pd.Series(k)

#SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()
text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#for loop to extract sentiment per title
title_neg_sent = []
title_pos_sent = []
title_neu_sent = []

length=len(data)
 
for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sent.append(neg)
    title_pos_sent.append(pos)
    title_neu_sent.append(neu)

title_neg_sent = pd.Series(title_neg_sent)
title_pos_sent = pd.Series(title_pos_sent)
title_neu_sent = pd.Series(title_neu_sent)

data['title_neg_sent']=title_neg_sent
data['title_pos_sent']=title_pos_sent
data['title_neu_sent']=title_neu_sent

data.to_excel('blogme_clean.xlsx', sheet_name='blogmedata', index=False)