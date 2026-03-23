print ("enter the number")
no=int(input())
p=0
temp=no
arm=0
while temp!=0:
	p=p+1
	temp=temp//10
temp=no
while temp!=0:
	r=temp%10
	arm=arm+r**p
	temp=temp//10
if arm==no:
	print(no," is armstrong number")
else:
	print(no," is not armstrong number")
