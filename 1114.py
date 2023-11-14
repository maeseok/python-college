'''test = {4,4,5,6,6,5,2,3}
#print(test)
majors= {"CS":"12","EE":"23","MS":45}
for i in majors:
    print(i)'''

a = [1,3,5,4,2]
a.sort(reverse=True)
print(a)

b=set()
test=[1,1,1,2,2,3,3,3,4,4,5]
for i in test:
    b.add(i)
print(b)

dic = {"T":"Tiger","C":"Cat","D":"Dog","B":"Bird"}
print(dic)
for i in dic.keys():
    dic[i]+="!"
print(dic)

tmp={}
A=[1,1,2,3,4,4,5,6]
A=['Tom', 'Mike' , 'Tom', 'Jerry', 'Mike', 'Steve']
for i in A:
    if i not in tmp:
        tmp[i]=1
    else:
        tmp[i]+=1
data=set(A)
for i,j in tmp.items():
    if j <=1:
        data.remove(i)
print(data)