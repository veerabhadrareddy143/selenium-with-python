from array import *
import numpy as np
"""for i in range(5):
    print(i*"*")   
""" # RAT
"""
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print(' ')
"""    #RAT numbeers
"""
b=0
for i in range(5,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b, end=' ')
    print(' ')
  #reverse RAT numbers
  """

n=5
k=2*n-2
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        print("* ",end="")
    print("")

"""
list=[]
list.append("veera")
list.insert(1,"bhadra")
print(list)
list.reverse()
print(list)
print(len(list))
print(type(list))
list.sort()
print(list)
list.append("reddy")
for i in list:
    print(i)
a=[2,5,32,34,25]
a.sort()
print(a)
l=np.array(list)
print(l)
"""

arr=[2,3,4,2,5,3,4]
print(len(arr))
arr.append(66)
str="veera"
print(len(str))
arr.reverse()
str1=''.join(reversed(str))
print(arr)
print(str1)
print(max(arr))






