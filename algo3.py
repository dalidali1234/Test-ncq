from collections import Counter
 
def solution(A):
    
    if len(A)==0: return 0
    if len(A)==1: return abs(A[0])
    a=[abs(s) for s in A]
    su=sum(a)
    ma=max(a)
    d=Counter(a)
    
    dp=[-1 for _ in range(2+1)]
    dp[0]=0
    for i in range(1,ma+1):
        if i not in d: continue
        for p in range(su//2+1):
            if dp [p]> = 0: dp [p] = d [i] 
                         elif p> = i and dp [pi]> 0: dp [p] = dp [pi] -1 
    for i in range(2,-1,-1):
        if dp[i]>=0: return su-2*i
 
 
print(solution([]))
print(solution([1,5,2,2]))
print(solution([1,5,2,-2]))
print(solution([1,2,100]))