for n in range(1,1001,1):
	p=0
	temp=n
	arm=0
	while temp!=0:
		p=p+1
		temp=temp//10
	temp=n
	while temp!=0:
		r=temp%10
		arm=arm+r**p
		temp=temp//10
	if arm==n:
		print(n," is armstrong number")