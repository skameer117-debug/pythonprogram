print("enter the number")
n=int(input())
es=0
os=0
while n!=0:
	r=n%10
	if r%2==0:
		es=es+r
	else:
		os=os+r
	n=n//10
print("no is odd digit=",os)
print("no is even digit",es)