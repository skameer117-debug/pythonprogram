print("enter the number")
n=int(input())
s=0
while n!=0:
	r=n%10
	print(r)
	n=n//10
print("sum of the digit",s)