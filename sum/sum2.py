print("enter the number")
n=int(input())
s=0
while n!=0:
	r=n%10
	s=s*10+r
	print(r)
	n=n//10
print("rev no=",s)