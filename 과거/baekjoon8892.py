import sys
from collections import deque
input=sys.stdin.readline
def palindrome(item):
    L1=[]
    L2=deque()
    for i in item:
        L1.append(i)
        L2.append(i)
    while(len(L1)>0 and L1.pop() == L2.popleft()):
        pass
    if len(L1)==0:
        return True
    else:
        return False
T=int(input())
for _ in range(T):
    k = int(input())
    for _ in range(k):
        item = input()
        palindrome(item)
