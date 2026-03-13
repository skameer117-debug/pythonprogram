print("enter the number")
n=int(input())
last=n%10
while n!=0:
	r=n%10
	n=n//10
print("first digit:",r+last)