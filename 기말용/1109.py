a=[1,3,5,4,2]
a.sort(reverse=True)
print(a)

a=[1,1,1,2,2,3,3,3,4,4,5]
a=set(a)
print(a)

data=["Tiger","Cat","Dog","Bird"]
dic={}
for i in data:
    print(i[0])
    dic[i[0]]=i+"!"
print(dic)

def name(list):
    res=set()
    for i in range(len(list)):
        if list.count(list[i])>1:
            res.add(list[i])
    return res

print(name(["Tom","Mike","Tom","Jerry","Mike","Steve"]))