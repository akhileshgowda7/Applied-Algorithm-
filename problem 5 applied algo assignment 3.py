#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import timeit
import matplotlib.pyplot as plt


def algorithm1(S):
    #S:sequence
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    return True


def algorithm2(S):
    #S:sequence
    S = sorted(S)
    for j in range(1, len(S)):
        if S[j-1] == S[j]:
            return False
    return True

def algorithm3(S, start, stop):
    #slice S[start:stop], S:sequence
    if stop - start <= 1: return True
    elif not algorithm3(S, start, stop-1): return False
    elif not algorithm3(S, start+1, stop): return False
    else: return S[start] != S[stop-1]
    
n=5000
a=[]
i=0
time_1_list = []

while n<=50000:
    rand=random.sample(range(n),n)
    a.append(len(rand))
    
    if __name__=="__main__":
        
        time_1=timeit.timeit("algorithm1(rand)","from __main__ import algorithm1,rand",number=1)
        time_1_list.append(time_1)
        if(time_1>45):
            print("The Largest value that the algorithm can run before 45s is ",a[i-1])
            break;
        n=n+5000
        i+=i
        
n=4000000
b=[]
i=0
time_2_list = []

while n<=100000000:
    rand=random.sample(range(n),n)
    b.append(len(rand))
    
    if __name__=="__main__":
        
        time_2=timeit.timeit("algorithm2(rand)","from __main__ import algorithm2,rand",number=1)
        time_2_list.append(time_2)
        if(time_2>45):
            print("The Largest value that the algorithm can run before 45s is ",b[i-1])
            break;
        n=n+4000000
        i+=i
        
n=1
c=[]
i=0
time_3_list = []

while n<=40:
    rand=random.sample(range(n),n)
    c.append(len(rand))
    
    if __name__=="__main__":
        
        time_3=timeit.timeit("algorithm3(rand,1,len(rand))","from __main__ import algorithm3,rand",number=1)
        time_3_list.append(time_3)
        if(time_3>45):
            print("The Largest value that the algorithm can run before 45s is ",c[i-1])
            break;
        n=n+1
        i+=i
        
plt.plot(a,time_1_list,label='algorithm1')
plt.title('algorithm1 Graph')
plt.xlabel('input')
plt.ylabel('Run Time')
plt.show()

plt.plot(b,time_2_list,label='algorithm2')
plt.title('algorithm2 Graph')
plt.xlabel('input')
plt.ylabel('Run Time')
plt.show()


plt.plot(c,time_3_list,label='algorithm3')
plt.title('Graph of algorithm 3')
plt.xlabel('input')
plt.ylabel('Run Time')
plt.show()


        




# In[ ]:




