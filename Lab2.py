def prime(n):
    for k in range(2,n):
            if(n % k==0):
                return False
    return True 

def gcd(m, n):
    k = m % n
    while k:
        m = n
        n = k
        k = m % n
    return n

def relatively_prime(m, n):
    return gcd(m, n) == 1