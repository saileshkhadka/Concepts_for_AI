
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


l=[1,2,3]
l


# In[5]:


a= np.array(l)
a


# In[6]:


type(l)


# In[7]:


a.shape


# In[8]:


a.ndim


# In[10]:


m=[[1,2,3],[4,5,6],[7,8,9]]


# In[19]:


np.array(m)


# In[17]:


a2=np.array(m)


# In[18]:


a2.ndim


# In[20]:


a2.shape


# In[22]:


np.arange(0,10,2)


# In[33]:


np.random.randn(5)


# In[32]:


np.random.randn(5,5)


# In[40]:


np.random.randint(1,10)


# In[41]:


np.random.randint(1,10,5)


# In[43]:


np.random.randint(1,10,(3,3))


# In[46]:


np.random.randint(1,10,(4,3,3))


# In[54]:


np.random.seed(9)
np.random.randint(1,10,7)


# In[55]:


arr = np.arange(12)
arr


# In[56]:


arr.shape


# In[57]:


arr.ndim


# In[60]:


arr.reshape(3,4)


# In[62]:


s=np.arange(10)
s


# In[63]:


s[1]


# In[64]:


s[-2]


# In[65]:


s[:]


# In[66]:


s[1:3]


# In[69]:


s[1:9:3]


# In[71]:


j = np.arange(10,20)
j


# In[73]:


j[0:5] = 200
j


# In[74]:


h=j[:7]
h


# In[76]:


h[:]=10
h


# In[77]:


j


# In[78]:


jc = np.copy(j)
jc


# In[79]:


jc[6:]=3
jc


# In[80]:


j


# In[81]:


np.random.seed(1)
abc=np.random.randint(1,10,(3,6))
abc


# In[84]:


abc[0,0]


# In[88]:


abc[1][2]


# In[89]:


abc[0]


# In[90]:


abc[2:, 2:]


# In[91]:


abc[1:,1:]


# In[92]:


a=np.arange(1,10)
a


# In[98]:


a[:-1]

