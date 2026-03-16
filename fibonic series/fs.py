term=int(input("enter the range"))
print("enter the number a")
a=int(input())
print("enter the number b")
b=int(input())
print(a,b,end="\t")
while term>2:
	c=a+b
	print(c,end="\t")
	a=b
	b=c
	term=term-1