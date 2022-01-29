#!/usr/bin/env python
# coding: utf-8

# In[107]:


def compare(x,y):
    (m1,n1)= x
    (m2,n2)= y
    if n1> n2 :
        return True
    else:
        return False
def minHeapify(l,n,i):
    lt= 2*i+1
    rt= 2*i+2
    smallest= i
    if (lt<n) and (compare(l[i],l[lt])):
        smallest= lt
    if (rt<n) and (compare(l[i],l[rt])):
        smallest= rt
    if (smallest !=i) :
        l[i],l[smallest]= l[smallest],l[i]
def buildMinHeap(l):
    l1= l.copy()
    n=len(l)
    if n == 0:
        return 0
    ln= n//2 -1 
    for i in range(ln,-1,-1):
        minHeapify(l,n,i)
    l1.remove(l[0])
    return l[0],l1


# In[140]:


def dijkstra2():
    inf= float('inf')
    md = {0:{1:50,2:30,3:100,4:10},
         1: {},
         2: {1:5},
         3: {1:20,2:50},
         4:{3:10}}
    dist = [(x,md[0][x] if x in md[0] else 0 if (x==0) else float('inf')) for x in md.keys()]
    print(dist)
    distHeap =dist[1:]
    n= len(distHeap)
    path=[]
    for x in range(n-1):
        (v,d), distHeap= buildMinHeap(distHeap)
        path+=[(v,d)]
        for y in range(len(distHeap)) :
            v2,d2 = distHeap[y]
            if (v2 in md[v].keys()):
                m = md[v][v2]
            else:
                m= inf
            mini = min (d2,d+m)
            distHeap[y]= (v2,mini)
           
    path+= distHeap
    print("final path: ",path)
    return 


# In[141]:


dijkstra2()


# In[ ]:




