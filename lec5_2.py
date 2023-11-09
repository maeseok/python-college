a=float(input("Side a :" ))
b=float(input("Side b :" ))
c=float(input("Side c :" ))
List=[a,b,c]
List.sort()
def check_tri(a,b,c):
    if abs(List[0])+abs(List[1])>abs(List[2]):
        print("YES")
    else:
        print("NO")
check_tri(a,b,c)