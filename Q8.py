'''h)
                 1    
            1 2  
         1 2 3 
    1 2  3 4 
 1 2 3  4 5'''
i = 1
while i<=5:
    j = 1
    while j<= 5-i:
        print(" ",end=" ")
        j+=1
    k = 1
    while k<=i:
        print(k,end=" ")
        k+=1
    print()
    i+=1