def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return 0
    else:
        return a/b
def pow(a,b):
    return a**b

a = int(input("a?"))
b = int(input("b?"))
print(add(a,b))
print(mul(a,b))
print(div(a,b))
print(pow(a,b))
