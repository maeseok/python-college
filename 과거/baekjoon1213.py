import sys
data = list(input())
data.sort()
tmp=[]
sol=[]
for i in data:
    if data.count(i)%2==0:
        tmp.append(i)
        for j in range(data.count(i)):
            data.remove(i)
if(len(data)==1):
    tmp.append(data[0])
    data.clear()
if(len(data)!=0):
    print(data)
    print("I'm Sorry Hansoo")
    quit()
sol=tmp+tmp.reverse()
print(sol)