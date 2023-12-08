a=[1,3,5,4,2]
a.sort(reverse=True)
print(a)

a=[1,1,1,2,2,3,3,3,4,4,5]
a=set(a)
print(a)

dict={}
data=["Tiger","Cat","Dog","Bird"]
for i in data:
    dict[i[0]]=i+"!"
print(dict)

A=[1,1,2,3,4,4,5,6]
A=["Tom","Mike","Tom","Jerry","Mike","Steve"]
dict={}
res=set()
for i in A:
    if A.count(i)>1:
        dict[i]=A.count(i)
print(dict)
for i in dict.keys():
    res.add(i)
print(res)