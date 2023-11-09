def fibonacci():
    List=[0,1]
    i=1
    while(1):
        tmp = List[i]+List[i-1]
        if(not tmp<1000):
            break
        List.append(tmp)
        i+=1
    return List
List = fibonacci()
print(List)