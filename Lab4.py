
graph1 = [ [1,2], [1,3], [3,4], [3,5], [4,5], [2,5] ]
graph2 = [ [1,3], [4,3], [3,5], [4,5], [1,6], [6,2], [6,5], [3,6] ]

graph3 = [ [1,2], [1,3], [3,4], [3,5], [4,5], [2,5] ] 
graph4 = [[1,3],[3,4],[3,5],[5,3]]

def subgraph(m,n):
    m.sort()
    n.sort()

    if(all(x in m for x in n )):
        print ("true") 
    else:
        print ("false")
       
def coloring(m):
    count1, count2, count3=0, 0, 0
    count4, count5, count6=0, 0, 0
    count7, count8, count9=0, 0, 0
    for x in m:
        for i in x:
            if(i == 1):
                count1+=1
            if(i == 2):
                count2+=1
            if(i == 3):
                count3+=1
            if(i == 4):
                count4+=1
            if(i == 5):
                count5+=1
            if(i == 6):
                count6+=1
            if(i == 7):
                count7+=1
            if(i == 8):
                count8+=1
            if(i == 9):
                count9+=1
        k = [count1, count2, count3, count4,count5,count6,count7,count8,count9]    
    print(f'{max(k)} is the minimum number of colors needed!')
           
           
def Euler(m):
    count1, count2, count3=0, 0, 0
    count4, count5, count6=0, 0, 0
    count7, count8, count9=0, 0, 0
    for x in m:
        for i in x:
            if(i == 1):
                count1+=1
            if(i == 2):
                count2+=1
            if(i == 3):
                count3+=1
            if(i == 4):
                count4+=1
            if(i == 5):
                count5+=1
            if(i == 6):
                count6+=1
            if(i == 7):
                count7+=1
            if(i == 8):
                count8+=1
            if(i == 9):
                count9+=1
        k = [count1,count2,count3,count4,count5,count6,count7,count8,count9]    
        if(any(k))
        


    #if (max(k)<2):
        #print("There is an Euler path as follow: ")
    #else:
        #print("empty")

     


#subgraph(graph1,graph2)

#coloring(graph3)

Euler(graph4)

