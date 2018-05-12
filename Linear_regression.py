
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[7]:


x=np.arange(-15,35,.5)


# In[8]:


x


# In[10]:


x=x.reshape(-1,1)


# In[16]:


m=0.7
c=3.78
y=m*x+c


# In[14]:


y[:10]


# In[18]:


plt.figure(figsize=(10,10))
plt.scatter(x,y,marker=".")
plt.grid()
plt.gca().set_aspect("equal")


# In[19]:


model1=LinearRegression()


# In[20]:


model1.fit(x,y)


# In[21]:


model1.coef_


# In[22]:


model1.intercept_


# In[23]:


model1.predict(36)


# In[24]:


#noise
x.shape


# In[25]:


np.random.seed(10)
noise=np.random.randn(x.shape[0],1)*2
noise[:10]


# In[26]:


plt.plot(noise)


# In[27]:


noise_y=y+noise


# In[28]:


plt.figure(figsize=(10,10))
plt.scatter(x,noise_y,marker=".")
plt.grid()
plt.gca().set_aspect("equal")


# In[30]:


model2=LinearRegression()


# In[31]:


model2.fit(x,noise_y)


# In[40]:


noise_y_pred=model2.predict(x)
plt.figure(figsize=(10,10))
plt.scatter(x,noise_y, marker=".", label="Actual")
plt.plot(x,noise_y_pred,color="r",label="Predicted")
plt.grid()
plt.legend()
plt.xlabel("X coor")
plt.ylabel("Y coor")
plt.gca().set_aspect("equal")

