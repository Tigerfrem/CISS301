def C(n):
    if(n==1):
        return 1
    elif(n==2):
        return 1
    elif(n == 0 or n < 0):
        print("Error: choose a positive number") 
    else:
        k = C(C(n-1)+C(n-C(n-1)))   
        return k

def A(n):
    if(n==1):
        return 1
    elif(n==2):
        return 1
    elif(n == 0 or n < 0):
        print("Error: choose a positive number")   
    else:
        m = A(A(n-1)+A(n-A(n-1)))   
        return m


print(C(0))    