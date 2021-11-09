#!/usr/bin/env python
# coding: utf-8

# In[12]:


n=int(input("enter the size"))


# In[30]:


arr=[None]*n
for i in range(n):
    val=int(input("enter the value"))
    arr[i]=val
print(arr)


# In[40]:


sum=0
for i in range(n):
    sum+=arr[i]
mean=sum/n    
print("mean is ",sum/n)    


# In[36]:


if(n%2==0):
    print("medianis ",(arr[n//2]+arr[(n//2)-1])/2)
else:
    print("median is",arr[n//2])


# In[41]:


## min max normalization
min=arr[0]
max=arr[0]
for i in range(n):
    if arr[i]<min:
        min=arr[i]
    if arr[i]>max:
        max=arr[i]
print(min,max)

for i in range(n):
    val=(arr[i]-min)/(max-min)
    print("normalization value is ",val)
import math
summ2=0
for i in arr:
    summ2=summ2+((i-mean)**2)
ans=math.sqrt(summ2/n)
print("std deviation ",ans) 
for i in range(n):
    val=(arr[i]-mean)/ans
    print("standardization ",val)


# In[ ]:




