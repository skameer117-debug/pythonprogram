print("enter the number")
n=int(input())
oc=0
ec=0
s=0
while n!=0:
	r=n%10
	if r%2==0:
		ec=ec+1
	else:
		oc=oc+1
	n=n//10
	s=ec+oc
print("no is odd digit=",oc)
print("no is even digit",ec)
print("sum of odd and even digit",s)