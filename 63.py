from math import log, floor

'''
Find x,n s.t.:
10^(n-1) <= x^n < 10^n

Note that if x=10, then x^n = 10^n, so x<10
'''

counter = 0

for x in range(1, 10):
    '''
    Now, we need to find an upper limit for n. We have that 
    10^(n-1) grows faster than x^n since x < 10, so we need
    to find n s.t.
    10^(n-1) = x^n
    10^n * 10^-1 = x^n
    0.1 * 10^n = x^n
    log(0.1 * 10^n) = log(x^n)
    log(0.1) + n * log(10) = n * log(x)
    n * (log(10) - log(x)) = -log(0.1) = log(10)
    n = log(10) / (log(10) - log(x))
    '''
    n_max = floor(log(10) / (log(10) - log(x)))
    for n in range(1, n_max + 1):
        y = x ** n
        l = len(str(y))
        if l == n:
            counter += 1

print(counter)