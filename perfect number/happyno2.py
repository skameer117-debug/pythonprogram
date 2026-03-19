n = int(input("Enter a number: "))
while n!=1 and n!=4:
    s = 0
    while n>0:
        r = n%10
        s = s+r * r
        n = n//10
    n = s
if n == 1:
    print("Khushi Number")
else:
    print("Dukhi number")