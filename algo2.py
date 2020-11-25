def solution(A, B):
    limit    = max(A)                
    result   = [0] * len(A)           
    modLimit = (1 << max(B)) - 1     
    fib    = [0] * (limit+2)
    fib[1] = 1
    for i in xrange(2, limit + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) & modLimit
    for i in xrange(len(A)):
        result[i] = fib[A[i]+1] & ((1<<B[i])-1)
    return result