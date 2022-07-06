
L = [[1,2],[1,1],[2,2],[3,3],[2,1],[1,4],[4,4]]
Q = [[1,2],[1,3],[3,1]]
S = [1,2,3,6]
R = [[1,2],[2,3],[1,3]]


def reflexive(L,S):
    count = 0
    for i1,i2 in L:
        if i1 | i2 in S:
            if (i1 == i2):   
                count+=1              
    if (count == len(S)):
        print("true")
        return True
    else:
        print("false")
        return False       



def symmetric(L):
    count = 0  
    for (i1,i2) in L:
        o = (i2,i1)
        if (o not in L):
            count+=1
    if count!=0:
        print ("false")
        return False
    else:
        print("true")
        return True



def transitive(L):
    if(len(L)>0):
        for p in L:
            a = p[0]
            b = p[1]
            for s in L:
                if s[0] == b:
                    c = s[1]
                    temp = [a, c]
                    if (temp not in L):
                        print("false")
                        return False        
       
    print ("true")
    return True




