#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Getting datasets
column_names=['user_id','item_id','rating','timestamp']
df=pd.read_csv('u.data',sep='\t',names=column_names)
movie_titles= pd.read_csv("Movie_Id_Titles")
df=pd.merge(df,movie_titles,on='item_id')
#Exploratory Data Analysis
sns.set_style('white')
#%matplotlib inline
df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
df.groupby('title')['rating'].count().sort_values(ascending=False).head()
ratings=pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['num of ratings']= pd.DataFrame(df.groupby('title')['rating'].count())
plt.figure(figsize=(10,4))
ratings['rating'].hist(bins=70) #Gausian Curve
plt.figure(figsize=(10,4))
ratings['num of ratings'].hist(bins=70)
sns.jointplot(x='rating',y='num of ratings',data=ratings,alpha=0.5)
#Recommending Movies
moviemat=df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()
ratings.sort_values('num of ratings',ascending=False).head(10)
starwars_user_ratings=moviemat['Star Wars (1977)']
starwars_user_ratings.head()
#Correlation
similar_to_starwars=moviemat.corrwith(starwars_user_ratings)
#Removing NaN values
corr_starwars= pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
#Filtering Data
corr_starwars=corr_starwars.join(ratings['num of ratings'])
corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head()