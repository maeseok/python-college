list=[0,1]
i=0
while(1):
    tmp = list[i]+list[i+1]
    if tmp<1000:
        list.append(tmp)
    else:
        break
    i+=1
print(list)