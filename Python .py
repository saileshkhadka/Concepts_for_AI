
# coding: utf-8

# In[2]:


print(5)


# In[4]:


print("Helloworld")


# In[5]:


a=1
print(a)


# In[8]:


a=b=c=1
a


# In[9]:


a=5
type(a)


# In[11]:


b='sailesh'
type(b)


# In[12]:


c=2.5
type(c)


# In[15]:


a="i'm sailesh"
print(a)


# In[17]:


print('{} is {} {}'.format("ghost","sailesh","germany"))


# In[20]:


a=[1,2,3,4]
print(a[2])


# In[21]:


b=[1,2,3,4]
len(b)


# In[22]:


a=[1,2,3,4,5]


# In[25]:


a[0]


# In[27]:





# In[28]:


a=[1,2,3]
print(a[0])


# In[29]:


a=[1,2,3,'hello']
a[0:]


# In[30]:


a[0:3]


# In[31]:


a=[1,2,3,4,5,6]
a[0:9:2]


# In[32]:


a=[1,2,3,4,5,6,7]
a[::-1]


# In[36]:


a[-5:-1]


# In[37]:


a=[1,2,3,4]
a.append(12)
a


# In[41]:





# In[43]:


a=[1,2,3,4]
a.append([7,8,9,10])
a


# In[46]:


a=[1,2,3]
a=b
a


# In[50]:


c=[4,5,6,7]


# In[51]:


'abc'+'abc'


# In[52]:


a=[4,5,6]
b=[7,8,9]
print(a+b)


# In[53]:


cat={
    'body':'fat',
    'color':'white',
    (1,2):'this is id'
}


# In[54]:


type(cat)


# In[57]:


cat['color']


# In[58]:


cat.keys()


# In[59]:


cat.values()


# In[60]:


cat.items()


# In[61]:


cat.update({'eyes':'blue'})


# In[62]:


cat


# In[65]:


cat['color']='blue'


# In[66]:


cat


# In[67]:


a=4


# In[68]:


type(a)


# In[69]:


b=str(a)
type(b)


# In[70]:


c="Hello"
type(c)


# In[71]:


"abc"+str(1)


# In[72]:


a=1
b=2
a==b


# In[74]:


def _add(a,b):
    c=a+b
    print(c)


# In[76]:


_add(4,5)


# In[77]:


_add("hello","world")


# In[81]:


def _sub(e,f):
    return e-f


# In[82]:


def g(x):
    return x,2,3


# In[83]:


g(2)


# In[86]:


def rel(a,b):
    if a==b:
        print("equal")
    elif a<b:
        print("lesser")
    else:
        print("greater")


# In[85]:


i=0
while(i!=5):
    print(i)
    i+=1


# In[91]:


for i in [1,2,3]:
      print(i)


# In[92]:


for i in range(0,10):
    print(i)


# In[94]:


for i in range(0,10,2):
    print(i)


# In[95]:


import numpy


# In[96]:


numpy.array([1,2])


# In[97]:


import numpy as np


# In[98]:


np.array([1,2])

