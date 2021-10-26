#!/usr/bin/env python
# coding: utf-8

# In[12]:


arr=[]
n=int(input("Enter the size of array "))
for i in range(n):
    ele=int(input())
    arr.append(ele)
for i in range(n-1):
    for j in range(i,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
summ=0            
for i in range(n):
    summ+=arr[i]
mean=summ/n
median=int(n/2)

print(arr)
print(mean)
print(arr[median])


# In[17]:


import numpy
y=numpy.std(arr)
print(y)
      


# In[22]:


import math
summ2=0
for i in arr:
    summ2+=(i-mean)**2
ab=math.sqrt(summ2/n)
print(ab)


# In[24]:


varience=ab**2
print(varience)

