import random

def drawing_integers(lb,ub,trials):
    List=[]
    for i in range(trials):
        List.append(random.randint(lb,ub))
    return List
def average_integers(List):
    avg=0
    sum=0
    for i in List:
        sum+=i
    avg = sum/len(List)
    return avg

def count_integers(List):
    data=[]
    Max = max(List)
    Min = min(List)
    for i in range(Min,Max+1):
        data.append((i,List.count(i)))
    return data
List=drawing_integers(1,5,5)
print(List)
print(average_integers(List))
print(count_integers(List))