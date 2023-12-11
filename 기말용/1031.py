def fibonacci():
    List=[0,1]
    i=0    
    while(1):
        data=List[i]+List[i+1]
        if not data<1000:
            break
        List.append(data)
        i+=1
    return List
print(fibonacci())

import random

def drawing_integers(lb,ub,trials):
    List=[]
    for i in range(trials):
        List.append(random.randint(lb,ub))
    return List
data=drawing_integers(1,5,5)
print(data)
def average_integers(list):
    return sum(list)/len(list)
print(average_integers(data))

def count_integers(list):
    res=[]
    Min=min(list)
    Max=max(list)
    for i in range(Min,Max+1):
        res.append((i,list.count(i)))
    return res

print(count_integers(data))