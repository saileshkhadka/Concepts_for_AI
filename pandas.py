
# coding: utf-8

# In[56]:


import numpy as np
import pandas as pd


# In[57]:


np.random.seed(10)
data_for_series=np.random.randint(0,100,size=(10))
data_for_series


# In[58]:


s=pd.Series(data_for_series)


# In[59]:


print(data_for_series)
s


# In[60]:


index_for_series='A B C D E F G H I J'.split()
index_for_series


# In[61]:


s=pd.Series(data_for_series,index=index_for_series)
s


# In[62]:


np.random.seed(10)
data=np.random.randint(0,10,(5,4))
data


# In[63]:


pd_frame=pd.DataFrame(data)
pd_frame


# In[64]:


my_index='A B C D E'.split()
my_column='M N O P '.split()
df=pd.DataFrame(data,my_index,my_column)
df


# In[65]:


df.describe()


# In[66]:


df.loc[['D','E']]


# In[67]:


df.iloc[[0,3]]


# In[68]:



df.iloc[:,1:3]


# In[69]:


df.loc[['D','E','C'],['N','O']]


# In[70]:


import os
os.getcwd()


# In[71]:


train_df=pd.read_csv('train.csv')
train_df


# In[72]:


train_df.head()


# In[73]:


train_df.tail()


# In[74]:


train_df.info()


# In[75]:


train_df.drop('Cabin',axis=1,inplace=True)


# In[76]:


train_df.head()


# In[77]:


train_df.drop(['Name','Ticket'],axis=1,inplace=True)
train_df


# In[78]:


train_df.head()


# In[79]:


train_df.info()


# In[80]:


null_embarked=train_df['Embarked'].isnull()


# In[81]:


null_embarked


# In[82]:


null_embarked.head()


# In[83]:


train_df[null_embarked]


# In[84]:


train_df['Embarked'].describe()


# In[85]:


train_df['Embarked'].fillna('S',inplace=True)
train_df.head()


# In[86]:


age_null=train_df['Age'].isnull()


# In[87]:


train_df[age_null]


# In[88]:


age_mean=train_df['Age'].mean()
age_mean


# In[89]:


train_df['Age'].fillna(age_mean,inplace=True)


# In[90]:


train_df.info()


# In[91]:


gender_map={
    'male':1,
    'female':2
}


# In[92]:


train_df['Sex']=train_df['Sex'].map(gender_map)


# In[93]:


train_df.head()


# In[94]:


dict_embark={
    'C':1,
    'S':2,
    'Q':3
}
train_df['Embarked']=train_df['Embarked'].map(dict_embark)


# In[95]:


train_df.info()


# In[98]:


train_df.to_csv("Titanic_train_numeric.csv",index=False)

