import random
def drawing_integers(lb,ub,trials):
    data=[]
    for i in range(trials):
        data.append(random.randint(lb,ub))
    return data
def average_integers(list):
    sum=0
    for i in list:
        sum+=i
    return sum/len(list)
def count_integers(list):
    res=[]
    Max=max(list)
    Min=min(list)
    for i in range(Min,Max+1):
        cnt = list.count(i)
        res.append((i,cnt))
    return res

data=drawing_integers(5,12,15)
aver=average_integers(data)
res = count_integers(data)
print(data)
print(aver)
print(res)

    