'''n)
0  
0 1  
0 2 4  
0 3 6 9  
0 4 8 12 16  '''
i = 1
c=0
while i <=5:
    j =0
    while j <i:
        print(j*c,end=" ")
        j+=1
    print()
    i+=1
    c+=1
    