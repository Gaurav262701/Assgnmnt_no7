#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Answer no 1
#program to find the sum of array
size = int(input("Enter the number of element you want in array"))
arr=[]
sum = 0
for i in range(0,size):
    elem=int(input("please give value of index"+str(i)+":"))
    arr.append(elem)
    sum+=elem
    
print("sum of array element =",sum)
    


# In[3]:


#Answer no 2
#program to find largest number in array
def largest(arr, n):
    max = arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [10,324,45,90,9008]
n = len(arr)
Ans = largest(arr,n)
print("Largest is given array",Ans)


# In[4]:


#Answer no 3
#program to rotate elements of array
def rotateArray(arr,n,d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] == arr[d]
        i = i +1
        d = d +1
        
    arr[:] = arr[: i] + temp
    return arr

arr = [1,2,3,4,5,6,]
print("Array after rotation is :",end = ' ')
print(rotateArray,len(arr),2)


# In[6]:


#Answer no 4
#program to split array and move first part to end
def splitArr(arr,n,k):
    for i in range(0,k):
        x = arr[0]
        for j in range(0,n-1):
            arr[j]= arr[j+1]
            
        arr[n-1] = x
        
arr = [12,10,5,6,52,36]
n = len(arr)
position = 2

splitArr(arr, n ,position)
for i in range(0,n):
    print(arr[i],end = ' ')


# In[9]:


#Answer no 5
#python program to check given array is monotonic
def isMonotonic(A):
    return (all(A[i]<=A[i+1]for i in range(len(A)-1)) or 
           all(A[i]>=A[i+1] for i in range(len(A)-1)))
A = [6,5,4,4]
print(isMonotonic(A))


# In[ ]:




