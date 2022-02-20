#!/usr/bin/env python
# coding: utf-8

# In[17]:


def compare(x,y):
    (m1,n1)= x
    (m2,n2)= y
    return True if n1> n2 else False
def minHeapify(l,n,i):
    lt= 2*i+1
    rt= lt+1
    smallest= i
    if (lt<n) and (compare(l[smallest],l[lt])):
        smallest= lt
    if (rt<n) and (compare(l[smallest],l[rt])):
        smallest= rt
    if (smallest !=i) :
        l[i],l[smallest]= l[smallest],l[i]
def buildMinHeap(l):
    n=len(l)
    if n == 0:
        return []
    ln= (n//2)-1
    for i in range(ln,-1,-1):
        minHeapify(l,n,i)
    return l

def extractNode(l):
     return buildMinHeap(l)[0] , l[1:]


# In[18]:


def dijkstra2():
    inf= float('inf')
    md = {0:{1:50,2:30,3:100,4:10},
         1: {},
         2: {1:5},
         3: {1:20,2:50},
         4:{3:10}}
    dist = [(x,md[0][x] if x in md[0] else 0 if (x==0) else float('inf')) for x in md.keys()]
    print("DistList: ", dist)
    distHeap =dist[1:]
    n= len(distHeap)
    path=[dist[0]]
    for x in range(n-1):
        (v,d), distHeap= extractNode(distHeap)
        path+=[(v,d)]
        for y in range(len(distHeap)) :
            v2,d2 = distHeap[y]
            m = md[v][v2] if (v2 in md[v].keys()) else inf          
            mini = min (d2,d+m)
            distHeap[y]= (v2,mini)
    path+= distHeap
    print("Final path: ",path)


# In[19]:


dijkstra2()

