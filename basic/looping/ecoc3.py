print("enter the number")
n=int(input())
es,os,ec,oc=0,0,0,0
while n!=0:
	r=n%10
	if r%2==0:
		es=es+r
		ec=ec+1
	else:
		os=os+r
		oc=oc+1
	n=n//10
print("no is odd digit=",oc)
print("no is even digit",ec)
print("sum of odd digit=",os)
print("sum of even digit",es)