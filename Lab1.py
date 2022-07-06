def fib(n):
    if(n==0):
        return 0
    elif (n==1):
        return 1
    elif (n<0):
        print("Enter a positive number")
    else: 
        k = fib(n-1)+fib(n-2)
        return k    


def luc(n):
    if (n==0):
        return 2
    elif (n==1):
        return 1
    elif (n<0):
        print("Enter a positive number")
    else:
        k = luc(n-1)+luc(n-2)
        return k

def pair(n): 
    a = n + 2
    b = n - 2
    c = None
    d = None
    if(a < 0):
        c = -fib(-a)
    else:
        c = fib(a)

    if(b < 0):
        d = -fib(-b)
    else:
        d = fib(b)
    return c - d



    '''4. What is the relationship between Luc and Pair? 

            Luc and Pair print the same values for n > 2. 
    
    '''


        

print(fib(1))
#print(luc(2))
#print(pair(2))
