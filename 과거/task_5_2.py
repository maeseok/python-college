a=[]
for _ in range(3):
    a.append(input())
a.sort()
if float(a[2])<(float(a[0])+float(a[1])):
    print("YES")
else:
    print("NO")