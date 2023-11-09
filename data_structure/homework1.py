#수행시간을 측정하는 코드
#Lee HyeongSeok 25/9/23

def sample(A, n):
    sum = 0
    k=n
    for i in range(0,k):
        for j in range(0,k):
            sum = sum +A[i]*A[j]
 
    return sum

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def dp_fibo(n):
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]


def hanoi(n, from_pos, to_pos, aux_pos,cnt):
    # 원반 n - 1개를 aux_pos로 이동(to_pos를 보조 기둥으로)
    cnt+=1
    hanoi(n - 1, from_pos, aux_pos, to_pos,cnt)
    # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로)
    hanoi(n - 1, aux_pos, to_pos, from_pos,cnt)
    return cnt



    
# 수행시간을 측정하는 코드
# blockdmask.-story.com/549
import math
import time 
import sys
sys.setrecursionlimit(10**6)
list=[]
#n=1000
#for i in range(n):
#    list.append(i)
start = time.time()
#sample(list,n)
#print("n=45")
#fib(45)
#print("n=193500")
#dp_fibo(193500)
print(hanoi(5, "a", "b", "c",0))  # 원반 한 개를 1번 기둥에서 3번 기둥으로 이동(2번을 보조 기둥으로)
end = time.time()
#print("n =",n)
print(f"{end - start:.5f} sec") # 소수점 5자리까지만 출력
