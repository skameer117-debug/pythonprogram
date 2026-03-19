for no in range(1,1001,1):
    temp=no
    while temp !=1 and temp !=4:
        s = 0
        while temp >0:
            r = temp%10
            s = s+r*r
            temp = temp//10
        temp = s
    if temp == 1:
        print(no,"Khushi Number")
    