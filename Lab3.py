def header():
    print("\n")
    print ("a     b     rem(a,b) = a - q * b") 
    print("---------------------------------")

header()
def kuttaka(m,n):
    m
    n
    k = m%n 
    q = m // n
    print(f'{m}   {n}     {k} = {m} - {q} * {n}')
    if (k != 0):
        kuttaka(n,k)
    elif(k == 0):
        print(f'{n}    {k} \n')
        print(f'Therefore, {n} is the gcd of')
    return m,n       

